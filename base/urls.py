from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('rooms/<int:id>/', views.room, name='topic'),
]
