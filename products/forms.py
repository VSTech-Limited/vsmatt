from django import forms
from .models import Product, ProductReview


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'tags', 'image', 'description', 'price', 'available', 'rating']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ('rating', "review")


class TagsFilterForm(forms.Form):
    tag = forms.BooleanField(required=False)


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Search for products"})
    )