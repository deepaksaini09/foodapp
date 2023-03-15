from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('best-rating-restaurants', views.bestRestaurantsByRatings, name="bestRestaurantsByRatings"),
    path('best-trending-restaurants', views.bestTrendingRestaurants, name='bestTrendingRestaurants'),
]
