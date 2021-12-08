from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import template
from django.conf import settings
from .models import Post,Author,Category,Tag
from django.http import HttpResponse , HttpResponseNotFound

def index(request):
    return HttpResponse("Hello World")

# def today_is(request):
#     now = datetime.datetime.now()
#     # t = template.loader.get_template('blog/datetime.html')
#     # c = template.Context({'now': now})
#     # html =  t.render(c)
#     # return HttpResponse(html)
#     return render(request,'blog/datetime.html', {'now':now , 
#                                                  'nav':'blog/nav.html',
#                                                  'base_dir':settings.BASE_DIR})

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})

def post_details(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Page not found");

    return render(request,"blog/post_detail.html",{'post':post})

def post_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/post_by_category.html', context)


# view function to display post by tag
def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/post_by_tag.html', context )