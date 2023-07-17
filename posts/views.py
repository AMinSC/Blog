from django.shortcuts import render
from django.views import View
from .models import Posts

# Create your views here.
class PostView(View):
    def get(self, request):
        posts = Posts.objects.all()
        context = {
            'title': 'Blog',
            'posts': posts,
        }
        return render(request, 'posts/post_list.html', context)
