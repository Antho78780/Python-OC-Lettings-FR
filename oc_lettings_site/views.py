from django.shortcuts import render

def index(request):
    """Return the request and the gabarit"""
    return render(request, 'index.html')

def error_404_view(request, exception):
    """Return the request and the gabarit for generate the error."""
    return render(request, '404.html')

def error_500_view(request, *args, **argv):
    """ Return the request object and the gabarit for generate the error."""
    return render(request, '500.html')
