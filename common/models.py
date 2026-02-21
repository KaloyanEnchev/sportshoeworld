from django.db import models

# Create your models here.
class Like(models.Model):
    to_photo = models.ForeignKey(
        "shoes.Shoe",
        on_delete=models.CASCADE,
    )