from django.test import TestCase
from shoes.models import Shoe, Category, Tag
from common.choices import BrandChoices, GenderChoices


class ShoeModelTests(TestCase):

    def test_create_shoe(self):
        shoe = Shoe.objects.create(
            brand=BrandChoices.NIKE,
            model="AirMax",
            gender=GenderChoices.MEN,
            size=42,
            color="Black",
            price=120,
            description="Comfortable shoes"
        )
        self.assertEqual(shoe.model, "AirMax")
        self.assertTrue(shoe.slug)

    def test_slug_generation(self):
        shoe = Shoe.objects.create(
            brand=BrandChoices.ADIDAS,
            model="Boost",
            size=44,
            color="White",
            price=150,
            description="Test"
        )
        self.assertIn("adidas-boost", shoe.slug)

    def test_string_representation(self):
        shoe = Shoe.objects.create(
            brand=BrandChoices.NIKE,
            model="Zoom",
            size=41,
            color="Red",
            price=100,
            description="Desc"
        )
        self.assertIn("Zoom", str(shoe))

    def test_category_str(self):
        category = Category.objects.create(sport="football")
        self.assertEqual(str(category), "Football")

    def test_tag_str(self):
        tag = Tag.objects.create(name="running")
        self.assertEqual(str(tag), "Running")