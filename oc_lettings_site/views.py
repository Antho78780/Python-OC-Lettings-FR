from django.shortcuts import render


def index(request):
    """La fonction index renvoie la requête et le gabarit"""
    return render(request, 'index.html')


def error_404_view(request, exception):
    """La fonction error404 renvoie la requête et le gabarit pour générer l'erreur."""
    return render(request, '404.html')


def error_500_view(request, *args, **argv):
    """La fonction error500 renvoie la requête et le gabarit pour générer l'erreur."""
    return render(request, '500.html')
