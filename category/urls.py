from django.urls import path

from category.views import ListCreateCategoryView

from .views import (
    ListCategoryView, RetrieveCategoryView,
    DestroyCategoryView, UpdateCategoryView, 
    ListCreateCategoryView )


urlpatterns = [
    path('lists/', ListCategoryView.as_view()),
    path('<int:pk>/', RetrieveCategoryView.as_view()),
    path('delete/<int:pk>/', DestroyCategoryView.as_view()),
    path('update/<int:pk>/', UpdateCategoryView.as_view()),
    path('create/', ListCreateCategoryView.as_view()),
]