from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    
class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    User = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)