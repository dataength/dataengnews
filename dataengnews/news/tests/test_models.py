from django.test import TestCase

from ..models import Item


class TestItem(TestCase):
    def test_model_should_have_url_field(self):
        expected = 'https://dataength.github.io/'
        Item.objects.create(url=expected)

        item = Item.objects.last()
        self.assertEqual(item.url, expected)
