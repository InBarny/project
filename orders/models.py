from django.db import models
from django.db import models
from main.models import Product
from users.models import User
from django.conf import settings
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.SET_DEFAULT,
        blank=True, 
        null=True, 
        default=None
    )
    first_name = models.CharField(
        max_length=50
    )
    last_name = models.CharField(
        max_length=50
    )
    email = models.EmailField(

    )
    city = models.CharField(
        max_length=100
    )
    address = models.CharField(
        max_length=250
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    paid = models.BooleanField(
        default=True
    )
    
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]
        
    
    def __str__(self):
        return f'Order {self.id}'
    
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        default=1
    )
    
    
    def __str__(self):
        return str(self.id)
    
    
    def get_cost(self):
        return self.price * self.quantity
    