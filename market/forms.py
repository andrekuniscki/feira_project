from django import forms
from .models import Item, Category

UNIT_CHOICES = [
    ('un','un'),
    ('kg','kg'),
    ('g','g'),
    ('l','l'),
    ('ml','ml'),
    ('pacote','pacote'),
]
class ItemForm(forms.ModelForm):
    unit = forms.ChoiceField(choices=UNIT_CHOICES, required=False, label='Unidade')
    bought = forms.BooleanField(required=False, label='Comprado')
    is_favorite = forms.BooleanField(required=False, label='⭐ Favorito')

    class Meta:
        model = Item
        fields = ['name', 'quantity', 'unit', 'category', 'price', 'notes', 'bought', 'is_favorite']
        labels = {
            'name': 'Nome',
            'quantity': 'Quantidade',
            'category': 'Categoria',
            'price': 'Preço (R$)',
            'notes': 'Notas',
        }