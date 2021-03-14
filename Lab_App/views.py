from django.http import HttpResponse

from .models import Experiments


# Create your views here.
def experiments_page(r):
    experiments = Experiments.objects.order_by('pk')
    list_experiments = ", ".join([experiment.name for experiment in experiments])
    return HttpResponse(list_experiments)
