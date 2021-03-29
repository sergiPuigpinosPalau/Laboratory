from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Experiment)
admin.site.register(Scientist)
admin.site.register(Article)

