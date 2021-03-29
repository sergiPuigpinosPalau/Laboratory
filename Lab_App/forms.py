from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
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


class ScientistSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = 'scientist'
        user.save()
        Scientist.objects.create(user=user)     #Create associated Model
        return user