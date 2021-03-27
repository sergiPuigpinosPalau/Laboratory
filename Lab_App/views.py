from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView


from Lab_App.models import *

# Create your views here.
def experiments_page(r):
    experiments = Experiment.objects.order_by('pk')
    list_experiments = ", ".join([experiment.name for experiment in experiments])
    return HttpResponse(list_experiments)


class ExperimentDetail(DetailView):
    model = Experiment
    template_name = 'experiment_detail.html'


def lab_home(request):
    article_list = Article.objects.order_by('-publish_date')
    scientist_list = Scientist.objects.order_by('-name')
    template = loader.get_template('laboratory_home.html')
    context = {
        'article_list': article_list,
        'scientist_list': scientist_list,
    }
    return HttpResponse(template.render(context, request))
