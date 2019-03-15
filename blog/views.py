from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models
def index(request):
    # return HttpResponse("Hello world!")
    article=models.Article.objects.all() # all返回查询集合（列表）
    return render(request, 'blog/index.html', {'article': article})

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')
    if str(article_id )== "0" :
        models.Article.objects.create(title=title,content=content)
        article = models.Article.objects.all()  # all返回查询集合（列表）
        return render(request, 'blog/index.html', {'article': article})
    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.content=content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})