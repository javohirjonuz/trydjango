from django import forms
from .models import Article
from django.forms import ValidationError


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'title',
            'class': 'form-control'
        })
        self.fields['image'].widget.attrs.update({
             'class': 'form-control'
        })

        self.fields['content'].widget.attrs.update({
            'cols': 60,
            'rows': 5,
            'placeholder': 'content',
            'class': 'form-control'

        })

    def clean_title(self):
        if self.cleaned_data['title'].replace(" ", '').isalpha():
            return self.cleaned_data['title']
        raise ValidationError('title must be alpha numeric')