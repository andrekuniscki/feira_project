from django.contrib import admin
from .models import Item, Category, ShoppingHistory, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'quantity', 'price', 'category', 'bought', 'is_favorite']
    list_filter = ['category', 'bought', 'is_favorite', 'created_at']
    search_fields = ['name']
@admin.register(ShoppingHistory)
class ShoppingHistoryAdmin(admin.ModelAdmin):
    list_display = ['owner', 'total_price', 'total_items', 'completed_at']
    list_filter = ['owner', 'completed_at']
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'favorite_market', 'currency', 'dark_mode']