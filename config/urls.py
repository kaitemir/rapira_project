from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from product.views import *
from django.conf.urls.static import static
from django.conf import settings



router = SimpleRouter()
router.register('products', ProductViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("account.urls")),
    path('category/', include('category.urls')),
    path('product/', include('product.urls')),
    path('favorites/', FavortiteView.as_view()),
    path('shoppingcart/', include('cart.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
