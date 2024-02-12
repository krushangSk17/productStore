from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    sku = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    stock_status = models.IntegerField(default=0)
    available_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = "0"

    def __str__(self):
        return self.name
