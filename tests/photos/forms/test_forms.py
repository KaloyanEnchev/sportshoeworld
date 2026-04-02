from django.test import TestCase
from shoes.forms import ShoeFormBasic


class ShoeFormTests(TestCase):

    def test_valid_form(self):
        form = ShoeFormBasic(data={
            "brand": "nike",
            "model": "Air",
            "gender": "men",
            "size": 42,
            "color": "Black",
            "price": 100,
            "description": "Nice shoes"
        })
        self.assertTrue(form.is_valid())

    def test_invalid_price(self):
        form = ShoeFormBasic(data={
            "brand": "nike",
            "model": "Air",
            "price": -5,
            "description": "Bad price"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("price", form.errors)

    def test_missing_required_fields(self):
        form = ShoeFormBasic(data={})
        self.assertFalse(form.is_valid())