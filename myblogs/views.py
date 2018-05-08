from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import BlogItems
from .forms import BlogItemForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    blogs = BlogItems.objects.filter(
        owner=request.user).order_by('-date_added')
    context = {}
    context['items'] = blogs
    return render(request, 'myblogs/index.html', context)


def add_blog(request):
    """add new blog"""
    if request.method != 'POST':
        form = BlogItemForm()
    else:
        form = BlogItemForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return HttpResponseRedirect(reverse('myblogs:index'))
    context = {'form': form}
    return render(request, 'myblogs/add_blog.html', context)


@login_required
def blog(request, blog_id):
    context = {}
    try:
        blog = BlogItems.objects.get(id=blog_id)
        context['blog'] = blog
        return render(request, 'myblogs/blog.html', context)
    except:
        return HttpResponse(" Can't find the blog, have you ever delete it before ")
