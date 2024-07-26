import unittest

from django.test import TestCase

from ads.models import Ad
from ads.serializers import AdSerializer


class AdSerializerTest(TestCase):

    def setUp(self):
        self.ad = Ad.objects.create(
            title='Test Ad',
            ad_id=1,
            author='Test Author',
            views=10,
            position=1
        )
        self.serializer = AdSerializer(instance=self.ad)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()),
                         set(['title', 'ad_id', 'author', 'views',
                              'position']))


if __name__ == '__main__':
    unittest.main()
