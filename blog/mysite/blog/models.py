from importlib.metadata import requires
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status = 'published')

class Post(models.Model):
    STATUS = (
        ("draft",'Draft'),
        ("published",'published')
    )
    RATING = (
        ("0",'0'),
        ("1",'1'),
        ("2",'2'),
        ("3",'3'),
        ("4",'4'),
        ("5",'5'),
    )
    slug = models.SlugField(max_length=250 , unique_for_date="publish" , blank=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS,default='draft')
    objects = models.Manager()
    published = PublishedManager()
    rating = models.CharField(max_length=10, choices=RATING,default='0')
    rating_user = models.ManyToManyField(User)
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year,self.publish.month,self.publish.day,self.slug])
    
    
    def __str__(self):
        return self.title
    
        


class Rating(models.Model):
    post = models.ForeignKey(Post,related_name='post_rate', on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_rate', on_delete=models.CASCADE)
    RATING = (
        ("0",'0'),
        ("1",'1'),
        ("2",'2'),
        ("3",'3'),
        ("4",'4'),
        ("5",'5'),
    )
    rating = models.CharField(max_length=10, choices=RATING , default='0')
    
    def ___str___(self):
        return self.rating