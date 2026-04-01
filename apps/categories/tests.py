from django.test import TestCase

from apps.categories.models import Category


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Personal")

        self.assertEqual(category.name, "Personal")
        self.assertEqual(category.icon, "tag")
