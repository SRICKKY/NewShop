from django.urls import path,include

from order_api.views import ItemInfoViewSet, ItemDetailInfoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product',ItemInfoViewSet)
router.register('product_details',ItemDetailInfoViewSet)

urlpatterns = [
	path('rest-auth/',include('rest_auth.urls')),
	path('rest-auth/registration/',include('rest_auth.registration.urls')),
]

urlpatterns += router.urls