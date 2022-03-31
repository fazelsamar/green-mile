from turtle import title
from django.db import models

# Create your models here.


class Province(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class City(models.Model):
#     province = models.ForeignKey(Province, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
