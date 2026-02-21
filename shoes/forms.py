from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse

from common.mixins import DisableFormFieldsMixin
from shoes.models import Shoe


class ShoeFormBasic(forms.ModelForm):
    class Meta:
        model = Shoe
        exclude = ['created_at', 'slug']
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'model': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter shoe model'
            }),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'size': forms.Select(attrs={'class': 'form-select'}),
            'color': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter color'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'placeholder': '0.00'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter shoe description'
            }),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        error_messages = {
            'model': {
                'required': 'Model name is required.',
                'max_length': 'Model name is too long.'
            },
            'price': {
                'required': 'Please enter a price.',
                'invalid': 'Enter a valid price.',
            },
            'size': {
                'required': 'Please select a size.',
            },
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise ValidationError("Price must be greater than 0.")
        return price

class ShoeCreateForm(ShoeFormBasic):
    ...

class ShoeEditForm(ShoeFormBasic):
    ...

class ShoeDeleteForm(DisableFormFieldsMixin, ShoeFormBasic):
    ...

class SearchForm(forms.Form):
    sport = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Search by sport...'}),
    )