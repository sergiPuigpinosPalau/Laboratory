from django.db import models


# Create your models here.
# Models/tables/classes that the DB will have
# After adding one, do
# python manage.py makemigrations webtodo  -- Creates file 001_initial, which will transform python to sql
# python manage.py migrate   --  uses function to transform the python table to sql
# or tools>manage.py

class Experiments(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    status = models.CharField(max_length=30)
    init_date = models.DateField()
