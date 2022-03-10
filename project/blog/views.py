from django.shortcuts import render
from .models import Article, Category


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
