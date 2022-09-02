from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    content = forms.CharField(label='Текст новости')
    published = forms.DateTimeField(label='Дата публикации')
    updated = forms.DateTimeField(label='Дата редактирования')
    is_published = forms.BooleanField(label='Опубликовано')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория')
