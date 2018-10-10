from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='log-home'),
    path('contact/', views.contact, name='log-contact')
]
