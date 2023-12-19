Views
=====

Views lettings
-------------- 

.. function:: index_letting(request)

    La vue index_letting va permettre d'afficher la liste des locations sur la page des locations

    ``letting_list = Letting.objects.all()`` est la liste des locations

    ``context = {letting_list: letting_list}`` est un dictionnaire qui va contenir la liste des locations et qui va être envoyé dans la template ``lettings/index.html``

    ``render()`` est la fonction qui va renvoyé la requête, le context et la template ce qui va donner ``render(request, context, lettings/index.html)``

.. function:: letting(request, letting_id)

    La vue letting permet à un utilisateur d'afficher une location en particulier

    ``letting = Letting.objects.get(id=letting_id)`` est la location 

    ``context = {title: letting.title, address: letting.address}`` est un dictionnaire qui va contenir le titre la location et l'adresse de la location

    ``render()`` est la fonction qui va renvoyé la requête, le context et la template ce qui va donner ``render(request, context, lettings/letting.html)``

Views profiles
-------------- 

.. function:: index_profile(request)

    La vue index_profile va permettre d'afficher la liste des profiles sur la page profiles

    ``profile_list = Profile.objects.all()`` est la liste des profiles

    ``context = {profile_list: profile_list}`` est un dictionnaire qui va contenir la la liste des profiles est qui va être envoyé dans la template ``lettings/index.html``

    ``render()`` est la fonction qui va renvoyé la requête, le context et la template ce qui va donner ``render(request, context, profiles/index.html)``

.. function:: profile(request, username_id)

    La vue profile permet à un utilisateur d'afficher un profile en particulier

    ``profile = Profile.objects.get(id=username_id)`` est le profile de l'utilisateur

    ``context = {profile: profile}`` est un dictionnaire qui va contenir le profile de l'utilisateur

    ``render()`` est la fonction qui va renvoyé la requête, le context et la template ce qui va donner ``render(request, context, lettings/letting.html)``
