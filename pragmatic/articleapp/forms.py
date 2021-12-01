from django.forms import ModelForm, fields, models
from django import forms
from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    class Meta:
        model = Article
        fields = ['title','image','project','content']