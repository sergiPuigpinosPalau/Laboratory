from django.forms import ModelForm

from Lab_App.models import *


class ArticleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        exPK = kwargs.pop('experimentpk', None)
        experiment = Experiment.objects.filter(pk=exPK).get()
        super(ArticleForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['author'].queryset = experiment.presentInExperiment.all()

    class Meta:
        model = Article
        exclude = ('user', 'date', 'experiment',)

