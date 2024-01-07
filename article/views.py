from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    old_articles = articles
    query = request.GET.get('q')
    articles = Article.objects.search(query=query)
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # if query:
    #     # articles = Article.objects.filter(title__icontains=query)
    #     articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        "object_list": page_obj,
        "old_articles_list": old_articles
    }
    return render(request, 'article/index.html', context)


def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        "object_detail": article
    }
    return render(request, 'article/detail.html', context)


def article_create(request):
    context = {
        'created': False
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        obj = Article.objects.create(title=title, content=content, image=image)
        context['created'] = True
        context['object'] = obj
        messages.success(request, "Article create")

    return render(request, 'article/create.html', context)


def article_create_form(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            obj = form.save()
            reverse_url = reverse('article:article_detail', args=[obj.id])
            messages.success(request, "Article create")
            return redirect(reverse_url)
    context = {
        'form': form
    }

    return render(request, 'article/create-form.html', context)


def article_create_form_(request):
    form = ArticleForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        obj = form.save()
        reverse_url = reverse('article:article_detail', args=[obj.id])
        return redirect(reverse_url)
    context = {
        'form': form
    }

    return render(request, 'article/create-form.html', context)


def article_edit(request, pk):
    obj = Article.objects.get(id=pk)
    form = ArticleForm(instance=obj)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=obj, files=request.FILES)
        if form.is_valid():
            form.save()
            reverse_url = reverse('article:change', kwargs={"pk": obj.id})
            messages.success(request, "Article Edit")
            return redirect(reverse_url)

    context = {
        'form': form,
        'object': obj,
    }
    return render(request, 'article/edit.html', context)


@login_required(login_url="auth:login")
@permission_required(perm="request.user.is_admin", login_url='/')
def article_delete(request, pk):
    obj = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, "Article delete")
        return redirect('article:article_list')
    context = {
        'object': obj
    }

    return render(request, 'article/delete.html', context)