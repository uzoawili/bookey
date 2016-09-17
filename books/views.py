from django.shortcuts import render, get_object_or_404
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
        c = request.GET.get('c')

        books = Book.objects.all()
        search_query = None
        if q:
            books = books.filter(name__icontains=q)
            search_query = q
        elif c:
            category = get_object_or_404(Category, pk=c)
            books = books.filter(category=category)
            search_query = category.name
        categories = Category.objects.all()

        context = {
            'categories': categories,
            'books': books,
            'search_query': search_query,
        }
        return render(request, 'books/home.html', context)




