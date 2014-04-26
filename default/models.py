from django.db import models

class Uni(models.Model):
    name = models.CharField(max_length=200)

class SpecCategoryCategory(models.Model):
    name = models.CharField(max_length=200)

class SpecCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(SpecCategoryCategory, related_name='categories')

class Programme(models.Model):
    categories = models.ManyToManyField(SpecCategory, related_name='programmes')
    uni = models.ForeignKey(Uni)
    description = models.TextField()
    name = models.CharField(max_length=200)

class PostCategory(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ManyToManyField(PostCategory, related_name='posts')
    date = models.DateField(auto_now=True)
    vote = models.IntegerField()
    programme = models.ForeignKey(Programme, related_name='posts')
