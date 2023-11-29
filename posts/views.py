from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def blog_list(request):
    #articles = Article.objects.all()
    articles = Article.publish.all()
    contex = {'articles':articles}
    return render(request,"blogs/list.html",contex)


def blog_detail(request,slug):
    article = Article.objects.get(slug=slug)
    contex = {'article' : article}
    return render(request,"blogs/detail.html",contex)




