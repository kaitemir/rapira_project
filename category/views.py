from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from category.models import Category
from category.permissions import IsAdminOrAllowAny
from category.serializers import CategorySerializer
import django_filters.rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter



class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrAllowAny,)  # is_staff = True

class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer
    http_method_names = ['get']
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ['title', 'price']
    search_fields = ['title', 'price', 'category']
    

class RetrieveCategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer

class DestroyCategoryView(generics.DestroyAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer

class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer
    
    