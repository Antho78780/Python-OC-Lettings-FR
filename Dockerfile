FROM python:3.10.9-alpine

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python manage.py collectstatic

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "oc_lettings_site.wsgi:application"]

