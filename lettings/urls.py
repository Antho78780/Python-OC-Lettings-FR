from django.urls import path
from . import views

urlpatterns = [
    path('lettings/', views.index, name='lettings_index'),
]
