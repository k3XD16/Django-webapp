from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('pixel/', views.pixel, name='pixel'),
    path('pixel/counter', views.counter, name='counter'),
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login')
]
