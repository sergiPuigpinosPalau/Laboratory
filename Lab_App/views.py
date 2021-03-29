from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from Lab_App.forms import ArticleForm, SignUpForm
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

    def get_form_kwargs(self):
        kwargs = super(CreateArticle, self).get_form_kwargs()
        kwargs['experimentpk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.experiment = Experiment.objects.get(id=self.kwargs['pk'])
        return super(CreateArticle, self).form_valid(form)

    def get_success_url(self):
        return reverse('Lab_App:experiment_details', kwargs={"pk": self.kwargs['pk']})


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'form.html'

    # In case you want to create specific sign ups / function to pass data to the form
    #
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'scientist'
    #     return super().get_context_data(**kwargs)
    #     pass

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Lab_App:home')
