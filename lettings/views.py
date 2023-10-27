from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """Return the request, the gabarit and the context which contains the list of profiles."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Return the request, the gabarit and the context which contains the profile."""
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
