from django.shortcuts import render
from .models import Article, Category


# Create your views here.
def index(request):  # index hamisha request qabul qiladi
    articles = Article.objects.all()  # maqolalar ruyxati
    print(articles)
    categories = Category.objects.all()
    print(categories)
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/index.html', context)
