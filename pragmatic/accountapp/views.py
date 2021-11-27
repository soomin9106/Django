from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView

from accountapp.forms import AccountUpdateForm

# Create your views here.

def hello_world(request):
    return render(request,'accountapp/hello_world.html')

#test321 4k4HszkCqJJnWq8
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class 에서 reverse 를 사용하면 에러가 난다.
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') #class 에서 reverse 를 사용하면 에러가 난다.
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'



