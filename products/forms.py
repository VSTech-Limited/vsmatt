from django import forms
from .models import Product


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'tags', 'image', 'description', 'price', 'available', 'rating']
