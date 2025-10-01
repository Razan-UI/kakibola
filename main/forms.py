from django.forms import ModelForm
from django import forms
from main.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "category","description", "thumbnail", "is_featured"]
        
