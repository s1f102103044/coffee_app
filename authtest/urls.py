from django.urls import path
from . import views

urlpatterns = [
    path('', views.recommend_coffee, name='recommend_coffee'),
    path('a', views.home, name='home'),
]