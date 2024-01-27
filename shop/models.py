from django.db import models

class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField()
    availiable = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)