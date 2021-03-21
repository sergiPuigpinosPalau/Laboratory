from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Experiment


# Create your views here.
def experiments_page(r):
    experiments = Experiment.objects.order_by('pk')
    list_experiments = ", ".join([experiment.name for experiment in experiments])
    return HttpResponse(list_experiments)


class ExperimentDetail(DetailView):
    model = Experiment
    template_name = 'experiment_detail.html'

    def get_context_data(self, **kwargs):

        context = super(ExperimentDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context