from django.shortcuts import render
from rest_framework import viewsets
from order_app.models import ItemInfo, ItemDetailInfo

from .serializers import ItemInfoSerializer, ItemDetailInfoSerializer

class ItemInfoViewSet(viewsets.ModelViewSet):
	queryset = ItemInfo.objects.all()
	serializer_class = ItemInfoSerializer

class ItemDetailInfoViewSet(viewsets.ModelViewSet):
	queryset = ItemDetailInfo.objects.all()
	serializer_class = ItemDetailInfoSerializer