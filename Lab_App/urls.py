from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url
from django.views.generic import DetailView
from Lab_App.models import *
from Lab_App.views import *

from . import views

urlpatterns = [
    path('experiments', views.experiments_page),
    url(r'^experiments/(?P<pk>\d+)/$', ExperimentDetail.as_view()),

]
