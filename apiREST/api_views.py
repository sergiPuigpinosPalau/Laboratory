from django.contrib import admin
from django.urls import path, include
from .api_views import *

urlpatterns = [
    # Login api points
    path('token/', token),
    path('token/refresh/', refresh_token),
    path('token/revoke/', revoke_token),
    path('token/revoke/', revoke_token),

    # Own api points
    path('', mainApi),
    # FOr the detail view and the list view, the same method
    path('restaurants/', api_restaurants_list),
    path('restaurants/<restaurant_pk>', api_restaurants_list),

]