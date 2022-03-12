from django.contrib import admin
from .models import Article, Category
from django.utils.safestring import mark_safe


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # bu class adminkada maqolaning qisqacha ta'rifini kursatib turish uchun
    list_display = ('pk', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    # adminkada shu yuqorida ko'rsatilganlar kurinib turadi
    list_display_links = ('pk', 'title')
    # shu ikkalasida ssilka bo'ladi
    list_editable = ('is_published',)

    # bu kimanda orqali adminkaning uzidan taxrirlash mumkin

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не найдено'

    get_photo.short_description = 'Фото'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
