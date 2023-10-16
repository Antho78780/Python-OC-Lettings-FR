from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.index, name='profiles_index'),
]
