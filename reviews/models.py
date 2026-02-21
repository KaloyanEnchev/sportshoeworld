from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

from common.vaidators import validate_review_body
from shoes.models import Shoe

class Review(models.Model):
    class ReviewType(models.TextChoices):
        TEXT = "Text", "Text"
        VIDEO = "Video", "Video"
        AUDIO = "Audio", "Audio"

    author_name = models.CharField(
        max_length=50,
        default="Anonymous"
    )
    body = models.TextField(
        validators=[
            validate_review_body
        ]
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
    )
    is_verified = models.BooleanField(
        default=False,
    )
    review_type = models.CharField(
        max_length=10,
        choices=ReviewType.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    shoe = models.ForeignKey(
        Shoe,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def clean(self) -> None:
        if self.shoe_id and not self.shoe.is_available:
            raise ValidationError("Cannot create review for unavailable shoe")

    def __str__(self):
        return f"{self.review_type} review ({self.rating}/5) for {self.shoe}"