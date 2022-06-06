from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import *

router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('category/', CategoryCreateView.as_view()),
    path('product/', include('product.urls')),
    path('favorites/', FavortiteView.as_view()),
]
