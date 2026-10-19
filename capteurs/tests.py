from django.test import TestCase
from django.urls import reverse

from .models import Capteur


class TestListeVide(TestCase):

    def test_liste_vide(self):

        # Vérifier que la base de test est vide
        self.assertEqual(Capteur.objects.count(), 0)

        # Accéder à la liste des capteurs
        reponse = self.client.get(
            reverse("capteurs:liste")
        )

        # Vérifier que la page fonctionne
        self.assertEqual(reponse.status_code, 200)

        # Vérifier le message de la liste vide
        self.assertContains(
            reponse,
            "Aucun capteur trouvé."
        )