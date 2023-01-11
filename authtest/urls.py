from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('priv1', views.private_page1, name='priv1'),
    path('priv2', views.private_page2, name='priv2'),
    path('priv3', views.private_page3, name='priv3'),
    path('pub', views.public_page, name='pub'),

    path('home/',views.index_1, name='home'),
    path('private1/',views.index_2, name='private1'),
    path('private2/',views.index_3, name='private2'),
    path('private3/',views.index_4, name='private3'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)