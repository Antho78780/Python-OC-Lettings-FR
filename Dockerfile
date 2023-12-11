# Image de base
FROM python:3.10.9-alpine

# Répertoire de travail
WORKDIR /app

# Copie du répertoire de travail
COPY . /app/

# Mise à jour de pip
RUN pip install --upgrade pip

# installations des packages
RUN pip install -r requirements.txt

# Mise à jour de la base de donnée
RUN python manage.py migrate

# Indication du port pour l'application
EXPOSE 8000

# La commande à exécuté au demmarage
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]

