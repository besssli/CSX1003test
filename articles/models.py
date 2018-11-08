from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    clap_num = models.IntegerField(default='0')
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[:50]+'...'


class Comment(models.Model):
    # post = models.ForeignKey('articles.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
