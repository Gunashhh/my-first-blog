from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.db.models import Q

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(~Q(yayinlanma_tarihi=None)).order_by('yayinlanma_tarihi')
    return render(request, 'blog/post_list.html', {'posts': posts})
