from django.test import TestCase
from django.contrib.auth.models import User
from market.models import Item, Category
from decimal import Decimal


class ItemModelTest(TestCase):
    """Testes para o modelo Item"""
    
    def setUp(self):
        """Criar usuário e categoria para os testes"""
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.category = Category.objects.create(name='Hortifruti', icon='🥬')
    
    def test_create_item(self):
        """Testar criação de um item"""
        item = Item.objects.create(
            name='Maçã',
            quantity=5,
            unit='kg',
            price=Decimal('10.00'),
            category=self.category,
            owner=self.user
        )
        self.assertEqual(item.name, 'Maçã')
        self.assertEqual(item.quantity, 5)
        self.assertEqual(item.owner, self.user)
    
    def test_item_get_total(self):
        """Testar cálculo de total do item"""
        item = Item.objects.create(
            name='Maçã',
            quantity=5,
            unit='kg',
            price=Decimal('10.00'),
            category=self.category,
            owner=self.user
        )
        self.assertEqual(item.get_total(), Decimal('50.00'))
    
    def test_item_default_bought_false(self):
        """Testar se item é criado como não comprado por padrão"""
        item = Item.objects.create(
            name='Maçã',
            quantity=5,
            unit='kg',
            price=Decimal('10.00'),
            category=self.category,
            owner=self.user
        )
        self.assertFalse(item.bought)
    
    def test_item_default_favorite_false(self):
        """Testar se item é criado como não favorito por padrão"""
        item = Item.objects.create(
            name='Maçã',
            quantity=5,
            unit='kg',
            price=Decimal('10.00'),
            category=self.category,
            owner=self.user
        )
        self.assertFalse(item.is_favorite)
    
    def test_item_string_representation(self):
        """Testar string representation do item"""
        item = Item.objects.create(
            name='Laranja',
            quantity=2,
            unit='kg',
            price=Decimal('8.00'),
            category=self.category,
            owner=self.user
        )
        self.assertEqual(str(item), 'Laranja (2 kg)')


class CategoryModelTest(TestCase):
    """Testes para o modelo Category"""
    
    def test_create_category(self):
        """Testar criação de categoria"""
        category = Category.objects.create(name='Limpeza', icon='🧹')
        self.assertEqual(category.name, 'Limpeza')
        self.assertEqual(category.icon, '🧹')
    
    def test_category_string_representation(self):
        """Testar string representation da categoria"""
        category = Category.objects.create(name='Bebidas', icon='🥤')
        self.assertEqual(str(category), '🥤 Bebidas')
    
    def test_retrieve_category(self):
        """Testar recuperação de categoria do banco"""
        Category.objects.create(name='Carnes', icon='🥩')
        retrieved = Category.objects.get(name='Carnes')
        self.assertEqual(retrieved.icon, '🥩')


class UserModelTest(TestCase):
    """Testes para o modelo de usuário (Django User)"""
    
    def test_create_user(self):
        """Testar criação de usuário"""
        user = User.objects.create_user(
            username='newuser',
            email='user@example.com',
            password='securepass123'
        )
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'user@example.com')
    
    def test_user_authentication(self):
        """Testar autenticação de usuário"""
        user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.assertTrue(user.check_password('testpass123'))
        self.assertFalse(user.check_password('wrongpassword'))
    
    def test_user_has_items(self):
        """Testar relação entre usuário e itens"""
        user = User.objects.create_user(username='itemuser', password='pass123')
        category = Category.objects.create(name='Test', icon='🔬')
        
        item1 = Item.objects.create(
            name='Item1',
            quantity=1,
            unit='un',
            price=Decimal('5.00'),
            category=category,
            owner=user
        )
        item2 = Item.objects.create(
            name='Item2',
            quantity=2,
            unit='un',
            price=Decimal('3.00'),
            category=category,
            owner=user
        )
        
        user_items = Item.objects.filter(owner=user)
        self.assertEqual(user_items.count(), 2)
