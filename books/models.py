from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    category =  models.ForeignKey(Category, related_name='books', null=True, blank=True)

    def __unicode__(self):
        return self.name
