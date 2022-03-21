from django.db import models


# Create your models here.

class PopularProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)
    stars = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        ordering = ['-updated_at']


class RecommendedProduct(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=200)
    stars = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        ordering = ['-updated_at']
