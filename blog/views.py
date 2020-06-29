from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})


#posts = Post.objects.filter( Published_date_lte = timezone.now() ).order_by('published_date')
# Post.objects.filter(published_date_lte=timezone.now()).order._by('published_date')
# to display in html we use {{posts}}
