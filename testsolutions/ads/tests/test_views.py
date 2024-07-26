import unittest

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ads.models import Ad


class AdViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.ad = Ad.objects.create(
            title='Test Ad',
            ad_id=1,
            author='Test Author',
            views=10,
            position=1
        )

    def test_list_ads(self):
        url = reverse('ad-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_ad(self):
        url = reverse('ad-detail', kwargs={'ad_id': self.ad.ad_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_ads_view(self):
        url = reverse('add_ads')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


if __name__ == '__main__':
    unittest.main()
