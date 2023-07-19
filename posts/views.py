from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from .forms import PostForm

# Create your views here.
class PostView(ListView):
    model = Posts
    template_name = 'posts/list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        context['search'] = ''
        return context


class PostDetail(DetailView):
    model = Posts
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_object(self):

        object = get_object_or_404(Posts, id=self.kwargs['post_id'])
        return object


class PostWrite(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['title', 'content', 'category']
    template_name = 'posts/write.html'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)


class PostEdit(UpdateView):
    model = Posts
    fields = ['title', 'content', 'category']
    template_name = 'posts/edit.html'
    context_object_name = 'post'
    success_url = reverse_lazy('blog:list')

    def get_object(self):

        object = get_object_or_404(Posts, id=self.kwargs['post_id'])
        return object


class PostDelete(DeleteView):
    model = Posts
    success_url = reverse_lazy('blog:list')

    def get_object(self):

        object = get_object_or_404(Posts, id=self.kwargs['post_id'])
        return object

# ?뒤에 커리문 처리 예정
class PostSerach(ListView):
    model = Posts
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = Posts.objects.all()

        tag = self.request.GET.get('tag', '')
        category = self.request.GET.get('category', '')

        if tag:
            queryset = queryset.filter(title__contains=tag)
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
