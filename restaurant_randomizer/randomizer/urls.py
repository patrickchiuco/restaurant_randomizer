from django.urls import path
from . import views


app_name = 'randomizer'

urlpatterns = [
	path('restaurant-list/', views.RestaurantListView.as_view(), name='restaurant-list'),
	path('restaurant-list/create/', views.RestaurantListCreateView.as_view(), name="restaurant-list-create"),
	path('restaurant-list/<int:pk>/', views.RestaurantListDetailView.as_view(), name="restaurant-list-detail"),
	path('restaurant-list/<int:pk>/edit/', views.RestaurantListUpdateView.as_view(), name="restaurant-list-update"),
	path('restaurant-list/<int:pk>/delete/', views.RestaurantListDeleteView.as_view(), name="restaurant-list-delete"),


	path('restaurant-list/<int:pk>/randomize/', views.randomize, name="randomize"),

	path('restaurant/create/<int:restaurant_list_id>', views.create_restaurant, name="restaurant-create"),
	path('restaurant/<int:pk>/', views.RestaurantDetailView.as_view(), name="restaurant-detail"),
	path('restaurant/<int:pk>/edit/', views.RestaurantUpdateView.as_view(), name="restaurant-update"),
	path('restaurant/<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name="restaurant-delete"),
	
	#path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),
	#path('notes/new/', views.NotesCreateView.as_view(), name="notes.new"),
]