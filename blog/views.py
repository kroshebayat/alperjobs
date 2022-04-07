from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def siteindex(request):
    return render(request, 'blog/siteindex.html')


def blogindex(request):
    return render(request, 'blog/blogindex.html')


def blogposts(request, post_slug):
    return HttpResponse(f"slug is {post_slug}")
