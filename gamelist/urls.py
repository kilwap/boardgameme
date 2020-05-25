from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name='home'),
	path('list/', views.game_list, name='list'),
	path('list/updatedb/', views.updatedb, name='updatedb'),

]