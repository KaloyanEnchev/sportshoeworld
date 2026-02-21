from django.db import models


class BrandChoices(models.TextChoices):
    ADIDAS = 'Adidas', 'Adidas'
    PUMA = "Puma", "Puma"
    NIKE = "Nike", "Nike"
    CHAMPION = "Champion", "Champion"
    NEW_BALANCE = "New Balance", "New Balance"


class SizeChoices(models.IntegerChoices):
    SIZE_37 = 37, '37'
    SIZE_38 = 38, '38'
    SIZE_39 = 39, '39'
    SIZE_40 = 40, '40'
    SIZE_41 = 41, '41'
    SIZE_42 = 42, '42'
    SIZE_43 = 43, '43'
    SIZE_44 = 44, '44'
    SIZE_45 = 45, '45'

class GenderChoices(models.TextChoices):
    MEN = "Men", "Men"
    WOMEN = "Women", "Women"
    UNISEX = "Unisex", "Unisex"