from django.db import models


class Uni(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpecCategoryCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpecCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        SpecCategoryCategory, related_name='categories')

    def __str__(self):
        return self.name


class Programme(models.Model):
    categories = models.ManyToManyField(
        SpecCategory, related_name='programmes')
    uni = models.ForeignKey(Uni)
    description = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(PostCategory, related_name='posts')
    date = models.DateField(auto_now=True)
    vote = models.IntegerField()
    programme = models.ForeignKey(Programme, related_name='posts')

    # FIXME: Use self.title
    def __str__(self):
        return self.text
