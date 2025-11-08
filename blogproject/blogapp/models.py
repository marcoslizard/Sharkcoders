from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __strt__(self):
        return self.title
# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE,related_name='comments')
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __strt__(self):
        return f'Comentário por {self.username}'