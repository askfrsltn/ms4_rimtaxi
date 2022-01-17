from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_trip, name="view_trip"),
    path('add/<tour_id>/', views.add_to_trip, name="add_to_trip"),
]
