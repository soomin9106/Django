from django.forms import ModelForm, fields, models
from articleapp.models import Article

class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','image','project','content']