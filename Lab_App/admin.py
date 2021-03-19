from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Experiments)
admin.site.register(Scientist)
admin.site.register(Article)
admin.site.register(Product)