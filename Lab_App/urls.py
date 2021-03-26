from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url
from django.views.generic import DetailView, ListView
from Lab_App.models import *
from Lab_App.views import *

from . import views

app_name = "Lab_App"

urlpatterns = [
    #path('experiments', views.experiments_page),

    #Experiment List
    url(r'^experiments/$', ListView.as_view(queryset=Experiment.objects.all().order_by('-init_date'),  #Query to get all experiments
                         context_object_name='exp_list_obj',  #variable where is stored
                         template_name='experiment_list.html')),

    #Experiment details
    url(r'^experiments/(?P<pk>\d+)/$', ExperimentDetail.as_view(), name='experiment_details'),

]
