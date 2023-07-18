from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Posts
from .forms import PostForm

# Create your views here.
class PostView(View):
    def get(self, request):
        posts = Posts.objects.all()
        context = {
            'title': 'Blog',
            'posts': posts,
            'search': ''
        }
        return render(request, 'posts/post_list.html', context)
    

class PostDetail(View):
    def get(self, request, post_id):
        post = Posts.objects.get(pk=post_id)
        context = {
            'post': post
        }
        return render(request, 'posts/post_detail.html', context)


class PostWrite(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'posts/post_write.html', context)
    
    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect('blog:list')
            # return redirect('/blog/detail/' + str(post.id))
        print(form)
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'posts/post_write.html')


class PostEdit(View):
    def get(self, request, post_id):
        post = Posts.objects.get(pk=post_id)
        form = PostForm(initial={
            'title': post.title,
            'content': post.content,
            'category': post.category,
        })
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'posts/post_edit.html', context)

    def post(self, request, post_id):
        post = Posts.objects.get(pk=post_id)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', post_id=post_id)
        
        form.add_error('폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'posts/post_list.html', context)


class PostDelete(View):
    def post(self, request, post_id):
        post = Posts.objects.get(pk=post_id)
        post.delete()
        return redirect('blog:list')


class PostSerach(View):
    def get(self, request, tag):
        if not tag:
            return redirect('blog:list')
        tag = request.GET.get('tag', '')
        print(tag)
        category = request.GET.get('category', '')
        print(category)
        # posts = Posts.objects.filter(title__contains=tag, category__exact=category)  # match

        posts = Posts.objects.all()
        if tag:
            posts = posts.filter(title__contains=tag)
        if category:
            posts = posts.filter(category=category)
        
        sort_order = request.GET.get('sort', 'newest')
        if sort_order == 'newest':
            posts = posts.order_by('-created_at')
        else:
            posts = posts.order_by('created_at') 
        
        context = {
            'title': 'Blog',
            'posts': posts,
        }
        return render(request, 'posts/post_list.html', context)
