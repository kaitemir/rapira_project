from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from category.models import Category
from category.permissions import IsAdminOrAllowAny
from category.serializers import CategorySerializer


class ListCreateCategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrAllowAny,)  # is_staff = True

class ListCategoryView(generics.ListAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer


class RetrieveCategoryView(generics.RetrieveAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer


class DestroyCategoryView(generics.DestroyAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all() # Ленивый запрос
    serializer_class = CategorySerializer


# class CreateCategoryView(generics.CreateAPIView):
#     queryset = Category.objects.all() # Ленивый запрос
#     serializer_class = CategorySerializer