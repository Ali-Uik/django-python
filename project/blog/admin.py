from django.contrib import admin
from .models import Article, Category


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # bu class adminkada maqolaning qisqacha ta'rifini kursatib turish uchun
    list_display = ('pk', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    # adminkada shu yuqorida ko'rsatilganlar kurinib turadi
    list_display_links = ('pk', 'title')
    # shu ikkalasida ssilka bo'ladi
    list_editable = ('is_published',)
    # bu kimanda orqali adminkaning uzidan taxrirlash mumkin


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
