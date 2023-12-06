from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """la fonction index renvoie la requête, le gabarit et le context  qui contient la liste des locations."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """La fonction letting renvoie la requête, le gabarit et le context qui contient la location."""
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
