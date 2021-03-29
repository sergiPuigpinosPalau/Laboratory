from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, TemplateView
from Lab_App.views import *


app_name = "Lab_App"

urlpatterns = [
    #Home
    path('', lab_home, name='home'),

    #Add article
    url(r'^experiments/(?P<pk>\d+)/articles/create/$', CreateArticle.as_view(), name='create_article'),

    # Experiment List
    url(r'^experiments/$',
        ListView.as_view(queryset=Experiment.objects.all().order_by('-init_date'),  # Query to get all experiments
                         context_object_name='exp_list_obj',  # variable where is stored
                         template_name='experiment_list.html'), name='experiments'),

    # Experiment details
    url(r'^experiments/(?P<pk>\d+)/$', ExperimentDetail.as_view(), name='experiment_details'),

    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/scientist/', ScientistSignUpView.as_view(), name='scientist_signup'),
    #path('accounts/signup/teacher/', AdministratorSignUpView.as_view(), name='administrator_signup'),

]
