from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.labels.models import Label

User = get_user_model()


class LabelModelTest(TestCase):
    def test_create_label(self):
        user = User.objects.create_user(username="label_user", password="pass1234")
        label = Label.objects.create(user=user, title="Home")

        self.assertEqual(label.title, "Home")
        self.assertEqual(label.user, user)
