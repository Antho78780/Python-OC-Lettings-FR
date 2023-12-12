from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """
    La fonction index renvoie la requête,
    le gabarit and le context qui contient la liste des profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    La fonction profile renvoie la requête,
    le gabarit et le context qui contient le profile.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
