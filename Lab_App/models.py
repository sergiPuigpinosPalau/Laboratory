from django.db import models

from phone_field import PhoneField


# Create your models here.
# Models/tables/classes that the DB will have
# After adding one, do
# python manage.py makemigrations webtodo  -- Creates file 001_initial, which will transform python to sql
# python manage.py migrate   --  uses function to transform the python table to sql
# or tools>manage.py

class Experiments(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=30)
    init_date = models.DateField()


class Scientist(models.Model):
    name = models.CharField(max_length=50)
    phone_numb = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField()
    position = models.CharField(max_length=30)


class Article(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    body = models.CharField(max_length=500)
    author = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    version = models.FloatField()
