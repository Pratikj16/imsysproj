from dataclasses import fields
from django import forms
from .models import Order, Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity']
        
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order 
        fields=['product','order_quantity']