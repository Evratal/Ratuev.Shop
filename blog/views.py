from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    queryset = Post.objects.filter(is_published=True)  # Пример фильтрации
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1
        post.save()
        return post

class PostCreateView(CreateView):
    model = Post
    fields = ("title","slug","content")
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    success_url = reverse_lazy("blog:post_detail")



class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")

