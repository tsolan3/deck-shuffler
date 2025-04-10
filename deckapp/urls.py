from django.urls import path
from . import views

urlpatterns = [
    path('api/shuffle/', views.api_shuffle, name='api_shuffle'),
    path('api/hall-of-fame/', views.hall_of_fame, name='hall_of_fame'),
    path('', views.main_page, name='main_page'),
]
