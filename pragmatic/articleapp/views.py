from django.db import models
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from articleapp.forms import ArticleCreationForm
from articleapp.decorators import article_ownership_required
from articleapp.models import Article

has_ownership = [article_ownership_required, login_required]


@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})

    def form_valid(self, form):
        temp_article = form.save(commit = False) #우리가 보낸 form => 임시 대기
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.pk})



@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginated_by = 25
