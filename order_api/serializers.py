from rest_framework import serializers

from order_app.models import ItemInfo, ItemDetailInfo

class ItemInfoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemInfo
		fields = ('id', 'url','name','author','price')

class ItemDetailInfoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ItemDetailInfo
		fields = ('id','url','name','unit_sold','date')