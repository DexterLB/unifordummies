from django.db import models

class Uni(models.Model):
    name = models.CharField(max_length=200)

class SpecCategory(models.Model):
    name = models.CharField(max_length=200)

class PostCategory(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(PostCategory)
    date = models.DateField(auto_now=True)
    vote = models.IntegerField()

class Programme(models.Model):
    categories = models.ManyToManyField(SpecCategory)
    uni = models.ForeignKey(Uni)
    description = models.TextField()
    name = models.CharField(max_length=200)
    posts = models.ForeignKey(Post)
