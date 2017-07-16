from django import forms
from .models import Category, Book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

    name = forms.CharField(label='Name', max_length=50)
    description = forms.CharField(label='Description', widget=forms.Textarea)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book

    name = forms.CharField(label='Name', max_length=50)
    author = forms.CharField(label='Author', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    category = forms.ModelChoiceField(label='Category',
                                      queryset=Category.objects.all(),
                                      empty_label='Select a Category')
