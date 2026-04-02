from django.test import TestCase
from reviews.models import Review
from shoes.models import Shoe
from common.choices import BrandChoices


class ReviewModelTests(TestCase):

    def setUp(self):
        self.shoe = Shoe.objects.create(
            brand=BrandChoices.NIKE,
            model="Test",
            size=42,
            color="Black",
            price=100,
            description="desc"
        )

    def test_create_review(self):
        review = Review.objects.create(
            body="Great",
            rating=4,
            review_type="Text",
            shoe=self.shoe
        )
        self.assertEqual(review.rating, 4)

    def test_string_representation(self):
        review = Review.objects.create(
            body="Nice",
            rating=5,
            review_type="Text",
            shoe=self.shoe
        )
        self.assertIn("5", str(review))

    def test_invalid_when_shoe_unavailable(self):
        self.shoe.is_available = False
        self.shoe.save()

        review = Review(
            body="Bad",
            rating=3,
            review_type="Text",
            shoe=self.shoe
        )

        with self.assertRaises(Exception):
            review.full_clean()