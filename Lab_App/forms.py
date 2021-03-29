from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import ModelForm
from django import forms

import Lab_App
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


class SignUpForm(UserCreationForm):

    user_type = forms.CharField(label='Type of account: ', widget=forms.Select(choices=User.USER_TYPE_CHOICES))
    name = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.user_type = self.cleaned_data.get('user_type')
        user.save()
        if user.user_type == 'scientist':
            scientist = Scientist.objects.create(user=user)     #Create associated Model
            scientist.name = self.cleaned_data.get('name')
            scientist.save()
        elif user.user_type == 'admin':
            admin = Administrator.objects.create(user=user)     #Create associated Model
            admin.name = self.cleaned_data.get('name')
            admin.save()
        return user