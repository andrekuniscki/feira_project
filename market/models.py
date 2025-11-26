from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, DecimalField
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=10, default='📦')
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f"{self.icon} {self.name}"

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=30, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    bought = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
    
    def get_total(self):
        return self.quantity * self.price

class ShoppingHistory(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shopping_history')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.PositiveIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-completed_at']
    
    def __str__(self):
        return f"Compra de {self.owner.username} - {self.completed_at.strftime('%d/%m/%Y')}"

class UserProfile(models.Model):
    CURRENCY_CHOICES = [
        ('BRL', 'R$ - Real'),
        ('USD', '$ - Dólar'),
        ('EUR', '€ - Euro'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture_url = models.CharField(max_length=500, blank=True, default='')
    favorite_market = models.CharField(max_length=120, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='BRL')
    dark_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
