from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Category

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

def create_default_categories():
    categories = [
        {'name': 'Hortifruti', 'icon': '🥬'},
        {'name': 'Limpeza', 'icon': '🧹'},
        {'name': 'Carnes', 'icon': '🥩'},
        {'name': 'Padaria', 'icon': '🍞'},
        {'name': 'Bebidas', 'icon': '🥤'},
        {'name': 'Lácteos', 'icon': '🥛'},
        {'name': 'Grãos', 'icon': '🌾'},
        {'name': 'Outros', 'icon': '📦'},
    ]
    for cat in categories:
        Category.objects.get_or_create(name=cat['name'], defaults={'icon': cat['icon']})