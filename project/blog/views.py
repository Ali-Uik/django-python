from django.shortcuts import render, redirect
from .models import Article, Category
from .forms import ArticleForm


# Create your views here.
def index(request):  # index hamisha request qabul qiladi
    articles = Article.objects.all()  # maqolalar ruyxati
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }
    return render(request, 'blog/all_articles.html', context)
    # request-zaprosiga javob beradi, context-dagi ma'lumotlarni 'blog/index.html'-ga jo'natadi


def category_list(request, pk):
    articles = Article.objects.filter(category_id=pk)
    # Article modelining ichidan category_id = zaprosdan kelgan pkga tengini chiqar
    # categories = Category.objects.all()
    context = {
        'articles': articles,
        # 'categories': categories
    }
    return render(request, 'blog/all_articles.html', context)


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'title': article.title,
        'article': article
    }
    return render(request, 'blog/details.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            return redirect('article_detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'title': 'Добавить статью',
        'form': form
    }

    return render(request, 'blog/article_form.html', context)
