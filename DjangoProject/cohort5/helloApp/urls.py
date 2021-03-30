from django.urls import  path
from . import views


urlpatterns  = [
    path('display/', views.display_html),
    path('callma/', views.call_mom)
]