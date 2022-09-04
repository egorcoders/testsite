from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Текст новости',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    published = forms.DateTimeField(label='Дата публикации')
    updated = forms.DateTimeField(label='Дата редактирования')
    is_published = forms.BooleanField(label='Опубликовано')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Выбор категории',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
