from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import DeleteView
from accountapp.decorators import account_ownership_required

from accountapp.forms import AccountUpdateForm

# Create your views here.

has_ownership = [account_ownership_required, login_required]

#soomin fndldishfwk99

@login_required
def hello_world(request):

    return render(request, 'accountapp/hello_world.html',context={'hello_world_list':"hello world"})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class 에서 reverse 를 사용하면 에러가 난다.
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') #class 에서 reverse 를 사용하면 에러가 난다.
    template_name = 'accountapp/update.html'

    
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'



