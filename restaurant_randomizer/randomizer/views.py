import datetime
import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import RestaurantList, Restaurant
from django.utils import timezone
from .forms import RestaurantListForm, RestaurantForm
from django.http import Http404, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class RestaurantListView(ListView):
	models = RestaurantList
	template_name = 'randomizer/restaurant_list.html'
	context_object_name = 'restaurant_list'

	def get_queryset(self):
		now = timezone.now()
		return RestaurantList.objects.filter(date_created__lte=now).order_by('-date_created')[:5]

class RestaurantListCreateView(CreateView):
	model = RestaurantList
	form_class = RestaurantListForm
	#context_object_name = 'list'
	success_url = '/randomizer/restaurant/create/'

class RestaurantListDetailView(DetailView):
	model = RestaurantList
	context_object_name = 'list'
	template_name = 'randomizer/restaurant_list_detail.html'


class RestaurantListUpdateView(UpdateView):
	model = RestaurantList
	form_class = RestaurantListForm
	success_url = '/randomizer/restaurant-list/'

class RestaurantListDeleteView(DeleteView):
	model = RestaurantList
	context_object_name = 'restaurant_list'
	success_url = '/randomizer/restaurant-list/'
	template_name = 'randomizer/restaurant_list_delete.html'


def create_restaurant(request, restaurant_list_id):
	if request.method == 'POST':
		model_form = RestaurantForm(request.POST)
		if model_form.is_valid():
			restaurant = model_form.save()
			return HttpResponseRedirect(reverse("randomizer:restaurant-list-detail", args=(restaurant.restaurant_list.id,)))
		else:
			return render(request, 'randomizer/restaurant_form.html', {'form': model_form, 'restaurant_list_id': restaurant_list_id})
	elif request.method == 'GET':
		model_form = RestaurantForm()
		return render(request, 'randomizer/restaurant_form.html', {'form': model_form, 'restaurant_list_id': restaurant_list_id})
	else:
		return HttpResponseBadRequest('Only GET and POsT are allowed.')

class RestaurantCreateView(CreateView):
	model = Restaurant
	form_class = RestaurantForm
	context_object_name = 'restaurant'
	
	def get_success_url(self):
		restaurant_list_id = self.object.restaurant_list.id
		return reverse('randomizer:restaurant-list-detail', kwargs={'pk':restaurant_list_id}) 

class RestaurantDetailView(DetailView):
	model = Restaurant
	context_object_name = 'restaurant'
	template_name = 'randomizer/restaurant_detail.html'

class RestaurantUpdateView(UpdateView):
	model = Restaurant
	form_class = RestaurantForm
	
	def get_success_url(self):
		restaurant_list_id = self.object.restaurant_list.id
		return reverse('randomizer:restaurant-list-detail', kwargs={'pk':restaurant_list_id}) 

class RestaurantDeleteView(DeleteView):
	model = Restaurant
	context_object_name = 'restaurant'
	template_name = 'randomizer/restaurant_delete.html'

	def get_success_url(self):
		restaurant_list_id = self.object.restaurant_list.id
		return reverse('randomizer:restaurant-list-detail', kwargs={'pk':restaurant_list_id}) 

def randomize(request, pk):
	restaurant_list = get_object_or_404(RestaurantList,pk=pk)
	no_of_restaurants = restaurant_list.restaurant_set.count()
	random_number = random.randrange(0, no_of_restaurants)
	restaurant = restaurant_list.restaurant_set.all()[random_number]
	return render(request, 'randomizer/randomizer_result.html', {'restaurant': restaurant,
		'restaurant_list': restaurant_list})

