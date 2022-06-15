from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import CategorySerializer
from .models import Favorite, Product, Likes
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters.rest_framework as filters
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .permissions import IsAuthororAdminPermission
from .paginations import ProductPagination
from .serializers import *

class CategoryCreateView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ['title', 'price']
    search_fields = ['title', 'price', 'category']
    pagination_class = ProductPagination
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser(), ]
        elif self.action in ['like', ]:
            return [IsAuthenticated()]
        return []    
    
    #products/id/like    
    @action(detail=True, methods=['GET'])
    def like(self, request, pk):
        product = self.get_object()
        user = request.user
        like_object, created = Likes.objects.get_or_create(product=product, user=user)
        if like_object.is_liked ==False:
            like_object.is_liked = not like_object.is_liked
            like_object.save()
            return Response('You liked this product')
        else:
            like_object.is_liked = not like_object.is_liked
            like_object.save()
            return Response('You disliked this product')
        
     #products/id/like    
    @action(detail=True, methods=['GET'])
    def favorite(self, request, pk):
        product = self.get_object()
        user = request.user
        fav, created = Favorite.objects.get_or_create(product=product, user=user)
        if fav.favorite ==False:
            fav.favorite = not fav.favorite
            fav.save()
            return Response('Added to favs')
        else:
            fav.favorite = not fav.favorite
            fav.save()
            return Response('Not in favs')


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, ]
    

class FavortiteView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        queryset = super().get_queryset()
        #                           model     FK                      model     boolean_field
        queryset = queryset.filter(favorites__user=self.request.user, favorites__favorite=True)
        return queryset