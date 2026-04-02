from django.test import TestCase
from django.urls import reverse
from reviews.models import Review
from shoes.models import Shoe
from common.choices import BrandChoices


class ReviewViewsTests(TestCase):

    def setUp(self):
        self.shoe = Shoe.objects.create(
            brand=BrandChoices.NIKE,
            model="Test",
            size=42,
            color="Black",
            price=100,
            description="desc"
        )

        self.review = Review.objects.create(
            body="Nice",
            rating=5,
            review_type="Text",
            shoe=self.shoe,
            is_verified=True
        )

    def test_list_view(self):
        response = self.client.get(reverse("reviews:list"))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(
            reverse("reviews:detail", kwargs={"pk": self.review.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_filter_by_type(self):
        response = self.client.get(reverse("reviews:list") + "?type=Text")
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get(reverse("reviews:list") + "?search=Nike")
        self.assertEqual(response.status_code, 200)

    def test_related_reviews_context(self):
        response = self.client.get(
            reverse("reviews:detail", kwargs={"pk": self.review.pk})
        )
        self.assertIn("related_reviews", response.context)