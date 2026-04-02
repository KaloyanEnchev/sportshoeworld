from django.test import TestCase
from django.urls import reverse
from shoes.models import Shoe, Category
from common.choices import BrandChoices, GenderChoices


class ShoeViewsTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(sport="football")

        self.shoe = Shoe.objects.create(
            brand=BrandChoices.NIKE,
            model="Test",
            gender=GenderChoices.MEN,
            size=42,
            color="Black",
            price=100,
            description="desc"
        )
        self.shoe.categories.add(self.category)

    def test_list_view(self):
        response = self.client.get(reverse("shoes:list"))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(
            reverse("shoes:shoe-detail", kwargs={"slug": self.shoe.slug})
        )
        self.assertEqual(response.status_code, 200)

    def test_filter_by_category(self):
        response = self.client.get(
            reverse("shoes:list") + f"?category={self.category.id}"
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.shoe.model)

    def test_men_filter(self):
        response = self.client.get(reverse("shoes:men-list"))
        self.assertEqual(response.status_code, 200)

    def test_pagination(self):
        for i in range(5):
            Shoe.objects.create(
                brand=BrandChoices.NIKE,
                model=f"Shoe{i}",
                size=42,
                color="Black",
                price=100,
                description="desc"
            )

        response = self.client.get(reverse("shoes:list"))
        self.assertTrue("page_obj" in response.context)