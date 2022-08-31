from tabnanny import verbose
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    content = models.TextField(
        max_length=255,
        blank=True,
        verbose_name='Текст'
    )
    published = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Опубликовано'
    )
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('title',)

    def get_absolute_url(self):
        return reverse('single_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-title',)

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self) -> str:
        return self.title
