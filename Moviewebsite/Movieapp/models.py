from django.db import models
from django.urls import reverse


# Create your models here.
class User_registration(models.Model):

    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True,unique=True)
    email = models.EmailField(max_length=240, null=True,unique=True)
    password = models.CharField(max_length=240, null=True,unique=True)

    def __str__(self):
        return self.firstname

class Add_movies(models.Model):
    movie_title=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    poster=models.ImageField(upload_to='gallery',blank=True)
    description=models.TextField(max_length=500,null=True)
    release_date=models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    actors=models.CharField(max_length=200,null=True)
    category=models.CharField(max_length=200,null=True)
    YouTube_trailer_link=models.CharField(max_length=200,null=True)

    class Meta:
        ordering = ('movie_title',)
        verbose_name = 'add movies'
        verbose_name_plural = 'add movies'

    def get_url(self):
        return reverse('category_slug',args=[self.slug])

    def __str__(self):
        return self.movie_title

class Category(models.Model):
    movie_title=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    category=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.movie_title