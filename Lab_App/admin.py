from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
admin.site.register(Experiment)
admin.site.register(Scientist)
admin.site.register(Article)
admin.site.register(Product)
admin.site.register(User, UserAdmin)
