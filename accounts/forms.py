from django import forms
from accounts.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        widgets = {
            "username": forms.TextInput(
                attrs={'placeholder': 'Username'},
            ),
            "email": forms.EmailInput(
                attrs={'placeholder': 'Email'},
            ),
            "age": forms.NumberInput(
                attrs={'placeholder': 'Age'},
            )
        }
