from django.forms import ModelForm, fields, models

from projectapp.models import Project


#Model Form
class ProjectCreationForm(ModelForm):
    class Meta: 
        model = Project
        fields = ['title','description','image']