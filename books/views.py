from django.shortcuts import render
from django.views.generic import View
from .models import Category, Book
# Create your views here.

class HomeView(View):
    """
    XXX
    """
    def get(self, request, *args, **kwargs):
        """
        handles get requests to the home route
        also handles search query param 'q'
        """
        q = request.GET.get('q')
        books = Book.objects.filter(name__icontains=q) if q else Book.objects.all()
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'books': books
        }
        return render(request, 'books/home.html', context)




