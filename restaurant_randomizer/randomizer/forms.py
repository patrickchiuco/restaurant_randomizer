from django import forms
from .models import RestaurantList, Restaurant

class RestaurantListForm(forms.ModelForm):
	class Meta:
		model = RestaurantList
		fields = ('user', 'list_name', 'description')

class RestaurantForm(forms.ModelForm):
	class Meta:
		model = Restaurant
		fields = ('restaurant_list', 'restaurant_name')
