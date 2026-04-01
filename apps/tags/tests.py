from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.tags.models import Tag

User = get_user_model()


class TagModelTest(TestCase):
    def test_create_tag(self):
        user = User.objects.create_user(username="tag_user", password="pass1234")
        tag = Tag.objects.create(user=user, name="Urgent")

        self.assertEqual(tag.name, "Urgent")
        self.assertEqual(tag.user, user)
