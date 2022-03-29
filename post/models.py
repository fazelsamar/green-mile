from django.db import models

from location.models import City
from account.models import MyUser

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_image/')
    description = models.TextField()
    postal_address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title


class PostComment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body


class PostLike(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title
