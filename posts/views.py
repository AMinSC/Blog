from typing import Any
from django.http import Http404, HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
class PostView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['search'] = ''
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_object(self):
        try:
            object = get_object_or_404(Post, id=self.kwargs['post_id'])
            object.update_counter()
            return object
        except Http404:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.get_object())
        return context


class PostWrite(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('accounts:login')
    model = Post
    fields = ['title', 'content', 'category', 'img']
    template_name = 'posts/write.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.save()
        return super().form_valid(form)


class PostEdit(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = Post
    fields = ['title', 'content', 'category', 'img']
    template_name = 'posts/edit.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:list')

    def get_object(self):

        object = get_object_or_404(Post, id=self.kwargs['post_id'])
        return object
    
    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.save()
        return super().form_valid(form)


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')

    def get_object(self):

        object = get_object_or_404(Post, id=self.kwargs['post_id'])
        return object

# ?뒤에 커리문 처리 예정
class PostSerach(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = Post.objects.all()

        tag = self.request.GET.get('tag', '')
        category = self.request.GET.get('category', '')

        if tag:
            queryset = queryset.filter(title__contains=tag) | queryset.filter(content__contains=tag)
        if category:
            queryset = queryset.filter(category=category)
        
        sort_order = self.request.GET.get('sort', 'newest')
        if sort_order == 'newest':
            queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.order_by('created_at')

        print(list(queryset))
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context
    

class CommentWrite(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/detail.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_id'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'post_id': self.object.post.pk})


class CommentDelete(DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'post_id': self.object.post.id})
