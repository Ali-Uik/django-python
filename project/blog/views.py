from django.shortcuts import render
from .models import Article, Category


# Create your views here.
def index(request):  # index hamisha request qabul qiladi
    articles = Article.objects.all()  # maqolalar ruyxati
    categories = Category.objects.all()
    context = {
        'articles': articles,
        'categories': categories
    }
    return render(request, 'blog/index.html', context)
    # request-zaprosiga javob beradi, context-dagi ma'lumotlarni 'blog/index.html'-ga jo'natadi
