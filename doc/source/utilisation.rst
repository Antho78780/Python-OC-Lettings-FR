Utilisation
===========

Installation
------------

Pour activer votre environnement virtuel utiliser la commande

.. code-block:: console

    (.venv) env/scripts/activate

Pour installer tout les packages utilieer la commande

.. code-block:: console

    (.venv) pip install -r requirements.txt


Lancement
---------

Pour actualiser les modèles dans la base de donnée utiliser la commande

.. code-block:: console

    (.venv) python manage.py migrate

Pour lancer le serveur utiliser la commande

.. code-block:: console

    (.venv) python manage.py runserver --insecure


Tests
-----

Pour executer vos tests verifier que vous étes dans le dossier PYTHON-OC-LETTINGS-FR et utiliser la commande

.. code-block:: console

    (.venv) pytest

Pour tester la couverture du code utiliser la commande

.. code-block:: console

    (.venv) coverage run -m pytest

Pour vour les resultats de la couverture de test vous pouvez utiliser la commande

.. code-block:: console

    (.venv) coverage report

Pour une présentation plus agréable de la couverture des tests, utiliser la commande

.. code-block:: console

    (.venv) coverage html

Pour vérifier que flake8 ne renvoie aucune erreur utiliser la commande

.. code-block:: console

    (.venv) flake8 lettings profiles oc_lettings_site

