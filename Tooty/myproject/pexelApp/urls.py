from django.urls import path
from . import views


urlpatterns  = [
    path('pexels/', views.sayHello)
]