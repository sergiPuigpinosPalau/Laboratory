from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from Lab_App.forms import ArticleForm
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


class CreateArticle(CreateView):
    model = Article
    template_name = 'form.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.experiment = Experiment.objects.get(id=self.kwargs['pk'])
        return super(CreateArticle, self).form_valid(form)

    def get_success_url(self):
        experiment = self.get_object(Experiment)
        return HttpResponseRedirect(reverse('Lab_App:experiment_details', args=self.object.id))
