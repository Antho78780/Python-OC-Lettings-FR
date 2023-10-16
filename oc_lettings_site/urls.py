from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path('', views.index, name='index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
