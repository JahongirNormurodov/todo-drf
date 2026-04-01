from django.test import TestCase

from apps.folders.models import Folder


class FolderModelTest(TestCase):
    def test_create_folder(self):
        folder = Folder.objects.create(name="Work")

        self.assertEqual(folder.name, "Work")
        self.assertEqual(folder.icon, "folder")
