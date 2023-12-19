Urls
====

``urlpatterns = []`` est une liste qui va contenir toute les urls du site web 

J'ai utilisé la fonction ``include()`` qui va permettre d'inclure les urls des application 


J'ai utilisé la fonction ``path()`` qui va contenir l'url et l'include

    ``urlpatterns = [``

    ``path("lettings/", include("lettings.urls")),``

    ``path("profiles/", include("profiles.urls")),``

    ``path('', views.index, name='index'),``

    ``path('admin/', admin.site.urls)``

    ``]``
