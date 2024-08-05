from django.db import models
class Shop(models.Model):
	Number=models.IntegerField()
	Color=models.CharField(max_length=64)
	Size=models.CharField(max_length=64)
	Quantity=models.IntegerField()
	Price=models.IntegerField()