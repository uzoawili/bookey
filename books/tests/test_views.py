from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from ..models import Book, Category

# Create your tests here.

class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.action_category = Category.objects.create(name='Action')
        self.romance_category = Category.objects.create(name='Romance')
        self.motiv_category = Category.objects.create(name='Motivational')

        self.fifty_book = Book.objects.create(name='Fifty', category=self.romance_category)
        self.bourne_book = Book.objects.create(name='The Bourne Identity', category=self.action_category)
        self.blah_book = Book.objects.create(name='Blah Blah')

    def test_homeview_returns_success(self):
        response = self.client.get(reverse('books:home'))
        self.assertEqual(response.status_code, 200)

    def test_homeview_search_by_name(self):
        response = self.client.get("{}?q={}".format(reverse('books:home'),'bour'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 1)
        self.assertEqual(response.context['books'].first(), self.bourne_book)

        response = self.client.get("{}?q={}".format(reverse('books:home'), 'dsbhckf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 0)

    def test_homeview_search_by_category(self):
        response = self.client.get("{}?c={}".format(reverse('books:home'), '3'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 0)

        response = self.client.get("{}?c={}".format(reverse('books:home'), '2'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['books'].count(), 1)
        self.assertEqual(response.context['books'].first(), self.fifty_book)

