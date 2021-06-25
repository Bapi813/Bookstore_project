from django.test import TestCase,client
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

from .models import Book,Review


class BookTests(TestCase):
    def setUp(self):
        self.user=get_user_model().objects.create_user(username='reviewuser',email='reviewuser@email.com',password='testpass123')
        self.book=Book.objects.create(title='Harry Potter',author='JK Rollwing', price='25.00')
        self.review=Review.objects.create(book=self.book,author=self.user,review='An excelent review',)
    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}','Harry Potter')
        self.assertEqual(f'{self.book.author}','JK Rollwing')
        self.assertEqual(f'{self.book.price}','25.00')
        
    def test_book_list_view(self):
        res=self.client.get(reverse('book_list'))
        self.assertEqual(res.status_code,200)
        self.assertContains(res,'Harry Potter')
        self.assertTemplateUsed(res,'books/book_list.html')
        
    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertContains(response,'An excelent review')
        self.assertTemplateUsed(response, 'books/book_detail.html')