from django.shortcuts import render , HttpResponse, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .forms import ArticleCreationForm
from .models import Article

# Create your views here.
class ArticleFormView(CreateView):
    template_name = "blog/article_form.html"
    form_class = ArticleCreationForm
    queryset = Article.objects.all()
    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = "blog/article_list.html"
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = "blog/article_detail.html"  
    queryset = Article.objects.all()

    # def get_object(self):
    #     _id = self.kwargs.get("id")
    #     return get_object_or_404(Article , id=_id)


class ArticleUpdateView(UpdateView):
    template_name = "blog/article_form.html"
    form_class = ArticleCreationForm
    queryset = Article.objects.all()

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Article , pk=_id)

    def form_valid(self , form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = "blog/article_delete.html"  

    def get_object(self):
        _id = self.kwargs.get("pk")
        return get_object_or_404(Article , id=_id)


    def get_success_url(self):
        return reverse("blog:index")