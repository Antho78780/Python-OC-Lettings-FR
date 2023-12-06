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

Pour une présentation plus agréable, utiliser la commande

.. code-block:: console

    (.venv) coverage html
