from django.urls import path, include
from . import views

urlpatterns = [
    path('current/', views.get_current_datetime)
]