from django.db import models
from django.forms import forms
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from profileapp.decorators import profile_ownership_required
from profileapp.models import Profile
from profileapp.forms import ProfileCreationForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

has_ownership = [profile_ownership_required, login_required]


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'taret_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit = False) #우리가 보낸 form => 임시 대기
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})


@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail',kwargs={'pk':self.object.user.pk})
