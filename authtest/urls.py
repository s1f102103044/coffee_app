from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('priv1', views.private_page1, name='priv1'),
    path('priv2', views.private_page2, name='priv2'),
    path('priv3', views.private_page3, name='priv3'),
    path('pub', views.public_page, name='pub'),
]