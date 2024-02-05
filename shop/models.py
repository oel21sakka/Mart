from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField()
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        url = reverse('product_view')
        url += f'?category__name={self.name}'
        return url

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    image = models.ImageField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def get_absolute_url(self):
        return reverse('product_detail_view', kwargs={'slug': self.slug})