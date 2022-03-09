from django.db import models


# Create your models here.
class Category(models.Model):
    # id в Django не пишется - она подставляется автоматически
    title = models.CharField(max_length=150, verbose_name='Название')

    # Char - simbollar, Field - qator. CharField - Simvollar qatori, verbose_name - adminkada kurinishi uchun

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Category (pk={self.pk}, title={self.title})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описение')  # blank=True - не обязательное для заполнения
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    # models.CASCADE - категория учирилганда шу категория билан боглик булган хамма статьяларни учиради

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Article (pk={self.pk}, title={self.title})'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
