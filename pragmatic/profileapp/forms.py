from django.forms import ModelForm, fields, models

from profileapp.models import Profile


#Model Form
class ProfileCreationForm(ModelForm):
    class Meta: 
        model = Profile
        fields = ['image','nickname','message']