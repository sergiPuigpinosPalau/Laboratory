from django.forms import ModelForm

from Lab_App.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ('user', 'date', 'experiment',)
