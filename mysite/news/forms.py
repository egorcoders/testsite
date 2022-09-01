from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.Textarea()
    published = forms.DateTimeField()
    updated = forms.DateTimeField()
    is_published = forms.BooleanField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
