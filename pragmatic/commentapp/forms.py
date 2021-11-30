from commentapp.models import Comment
from django.forms import ModelForm, fields

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']