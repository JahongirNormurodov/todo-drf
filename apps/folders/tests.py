from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.folders.models import Folder

User = get_user_model()


class FolderModelTest(TestCase):
    def test_create_folder(self):
        user = User.objects.create_user(username="folder_user", password="pass1234")
        folder = Folder.objects.create(user=user, name="Work")

        self.assertEqual(folder.name, "Work")
        self.assertEqual(folder.user, user)
