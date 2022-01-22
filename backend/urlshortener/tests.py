from base64 import b64encode
from django.core.cache import cache
from rest_framework import status
from rest_framework.test import APITestCase
from urlshortener.models import Shortener


class AccountTests(APITestCase):
    def test_create_shorturl(self):
        data = {'long_url': 'https://www.django-rest-framework.org/api-guide/testing/'}
        response = self.client.post('/api/shorturl/v1', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'short_url': b'MQ=='})

        # test cache
        url = cache.get(1)
        self.assertEqual(url, data['long_url'])

    def test_get_shorturl(self):
        sh = Shortener.objects.create(long_url='https://www.django-rest-framework.org/api-guide/testing/')

        shorturl = b64encode(str(sh.id).encode('utf-8'))
        response = self.client.get(f'/api/shorturl/v1/{shorturl.decode("utf-8")}', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(sh.long_url, response.data['long_url'])

        # test cache
        url = cache.get(2)
        self.assertEqual(url, sh.long_url)
