from django.test import TestCase
from reviews.forms import ReviewForm


class ReviewFormTests(TestCase):

    def test_valid_form(self):
        form = ReviewForm(data={
            "body": "Good",
            "rating": 4,
            "review_type": "Text"
        })
        self.assertTrue(form.is_valid())

    def test_invalid_rating(self):
        form = ReviewForm(data={
            "body": "Bad",
            "rating": 10,
            "review_type": "Text"
        })
        self.assertFalse(form.is_valid())

    def test_missing_fields(self):
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())