from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """Return the request, the gabarit and the context which contains the list of profiles."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Return the request, the gabarit and the context which contains the profile."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
