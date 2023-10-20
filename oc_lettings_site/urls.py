from django.contrib import admin
from django.urls import path, include
from . import views




# def trigger_error(request):
#     division_by_zero = 1 / 0
#     return division_by_zero


urlpatterns = [
    # path('sentry-debug/', trigger_error),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]

