import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_recipe.settings")
import django
django.setup()

from django.urls import reverse
from django.test import TestCase

from recipe.models import Category

class MainViewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertContains(response, self.category.name)
