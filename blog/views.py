from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    def get(self, request):
        posts = Post.objects.filter(is_published=True)
        return render(request, 'blog/post_list.html', {'posts': posts})


class PostDetailView(DetailView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.views_count += 1
        post.save()  # Увеличиваем счетчик просмотров
        return render(request, 'blog/post_detail.html', {'post': post})


class PostCreateView(CreateView):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        return render(request, 'blog/post_form.html', {'form': form})


class PostUpdateView(UpdateView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)  # Перенаправление на детальный просмотр
        return render(request, 'blog/post_form.html', {'form': form})


class PostDeleteView(DeleteView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')