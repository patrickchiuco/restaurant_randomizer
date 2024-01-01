from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class RestaurantList(models.Model):
	list_name = models.CharField(max_length=200)
	description = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.list_name

class Restaurant(models.Model):
	restaurant_list = models.ForeignKey(RestaurantList, on_delete=models.CASCADE)
	restaurant_name = models.CharField(max_length=200)

	def __str__(self):
		return self.restaurant_name