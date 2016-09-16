from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    category =  models.ForeignKey(Category, related_name='books')
