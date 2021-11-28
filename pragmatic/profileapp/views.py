from django.db import models
from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'taret_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit = False) #우리가 보낸 form => 임시 대기
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)