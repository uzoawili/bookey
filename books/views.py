from django.shortcuts import render
from django.views.generic import View
from .models import Category, Book
# Create your views here.

class HomeView(View):
    """
    XXX
    """

    def get(self, request, *args, **kwargs):
        """handles get requests to the home route"""
        # url_params = request.GET
        categories = Category.objects.all()
        books = Book.objects.all()
        context = {
            'categories': categories,
            'books': books
        }
        return render(request, 'books/home.html', context)




