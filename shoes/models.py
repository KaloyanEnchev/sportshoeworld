from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from accounts.models import Account
from common.choices import SizeChoices, BrandChoices, GenderChoices
from common.vaidators import validate_description_length, validate_image_size


class Shoe(models.Model):
    brand = models.CharField(
        max_length=100,
        choices=BrandChoices.choices
    )
    model = models.CharField(
        max_length=100
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default=GenderChoices.UNISEX,
    )
    size = models.IntegerField(
        choices=SizeChoices.choices,
        null=True,
        blank=True
    )
    color = models.CharField(
        max_length=50
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.00)]
    )
    categories = models.ManyToManyField(
        'Category',
        related_name="shoes",
        blank=True,
    )
    is_available = models.BooleanField(
        default=True
    )
    description = models.TextField(
        validators=[
            validate_description_length
        ]
    )
    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
        validators=[
            validate_image_size
        ]
    )
    slug = models.SlugField(
        unique=True,
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.brand}-{self.model}-{self.size}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.size}"


class Category(models.Model):
    sport = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.sport