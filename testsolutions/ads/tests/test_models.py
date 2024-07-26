import unittest

from django.test import TestCase

from ads.models import Ad


class AdModelTest(TestCase):

    def setUp(self):
        self.ad = Ad.objects.create(
            title='Test Ad',
            ad_id=1,
            author='Test Author',
            views=10,
            position=1
        )

    def test_ad_creation(self):
        self.assertIsInstance(self.ad, Ad)
        self.assertEqual(self.ad.__str__(), self.ad.title)


if __name__ == '__main__':
    unittest.main()
