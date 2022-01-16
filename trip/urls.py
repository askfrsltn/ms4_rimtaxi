from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_trip, name='view_trip'),
]