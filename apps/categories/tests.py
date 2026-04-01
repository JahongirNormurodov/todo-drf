from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.categories.models import Category

User = get_user_model()


class CategoryModelTest(TestCase):
    def test_create_category(self):
        user = User.objects.create_user(username="cat_user", password="pass1234")
        category = Category.objects.create(user=user, name="Personal")

        self.assertEqual(category.name, "Personal")
        self.assertEqual(category.user, user)
