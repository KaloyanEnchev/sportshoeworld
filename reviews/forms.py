from django import forms
from django.core.exceptions import ValidationError

from common.mixins import DisableFormFieldsMixin
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['created_at', 'user']

        labels = {
            'rating': 'Your Rating',
            'comment': 'Your Review',
        }

        help_texts = {
            'rating': 'Rate from 1 (worst) to 5 (best).',
        }

        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Share your experience with this shoe...'
            }),
        }

        error_messages = {
            'rating': {
                'required': 'Please select a rating.',
            },
        }

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and rating > 5:
            raise ValidationError("Rating cannot be higher than 5.")
        return rating

class ReviewCreateForm(ReviewForm):
    ...

class ReviewEditForm(ReviewForm):
    ...

class ReviewDeleteForm(ReviewForm, DisableFormFieldsMixin):
    ...