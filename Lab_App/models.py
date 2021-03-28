from django.contrib.auth.models import AbstractUser
from django.db import models

from phone_field import PhoneField


# Create your models here.
# Models/tables/classes that the DB will have
# After adding one, do
# python manage.py makemigrations webtodo  -- Creates file 001_initial, which will transform python to sql
# python manage.py migrate   --  uses function to transform the python table to sql
# or tools>manage.py


class User(AbstractUser):
    USER_TYPE_CHOICES = [('SC', 'Scientist'), ('ADM', 'Admin'), ]
    user_type = USER_TYPE_CHOICES


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='Administrator_profile')


class Experiment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=30)
    init_date = models.DateField()

    def __str__(self):
        return str(self.name)


class Scientist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='Scientist_profile')
    name = models.CharField(max_length=50)
    phone_numb = PhoneField(blank=True, help_text='Contact phone number')
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    birth_date = models.DateField()
    position = models.CharField(max_length=30)
    experiment = models.ForeignKey(Experiment, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    body = models.TextField(max_length=500)
    author = models.ForeignKey(Scientist, null=True, on_delete=models.PROTECT)
    experiment = models.ForeignKey(Experiment, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    version = models.FloatField()
    experiment = models.ForeignKey(Experiment, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.name)
