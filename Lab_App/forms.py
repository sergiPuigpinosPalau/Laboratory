from django.forms import ModelForm

from Lab_App.models import *


class ArticleForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)  # populates the post
        #self.fields['author'].queryset = Scientist.objects.filter(experiment=)


    class Meta:
        model = Article
        exclude = ('user', 'date', 'experiment',)

