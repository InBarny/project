from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True
    )
    slug = models.SlugField(
        max_length=20,
        unique=True
    )
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def get_absolute_url(self):
        return reverse("main:product_list_by_category",
                       args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        to='Category',
        related_name='Продукт',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50
    )
    slug = models.SlugField(
        max_length=50
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )
    available = models.BooleanField(
        default=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    discount = models.DecimalField(
        default=0,
        max_digits=4,
        decimal_places=0
    )
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:product_detail',
                       args=[self.slug])
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 0)
        return self.price
        