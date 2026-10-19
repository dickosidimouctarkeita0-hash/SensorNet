from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Capteur


class CapteurAPITests(APITestCase):

    def test_liste_capteurs(self):
        url = reverse('capteurs-list')
        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_post_interdit(self):
        url = reverse('capteurs-list')
        response = self.client.post(url, {})

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_put_interdit(self):
        url = reverse('capteurs-detail', args=[1])
        response = self.client.put(url, {})

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_delete_interdit(self):
        url = reverse('capteurs-detail', args=[1])
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )