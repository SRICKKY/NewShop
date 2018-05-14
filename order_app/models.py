from django.db import models

# Create your models here.

class ItemInfo(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	price = models.CharField(max_length=5)

	def __str__(self):
		return self.name


class ItemDetailInfo(models.Model):
	name = models.ForeignKey(ItemInfo, on_delete=models.CASCADE)
	unit_sold = models.CharField(max_length=10)
	date = models.DateField()

	# def __str__(self):
	# 	return self.name