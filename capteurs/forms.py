from django import forms


class RechercheCapteurForm(forms.Form):

    q = forms.CharField(
        label="Nom du capteur",
        max_length=40,
        required=False
    )

    actifs_seulement = forms.BooleanField(
        label="Capteurs actifs seulement",
        required=False
    )

from .models import Capteur


# Formulaire pour ajouter ou modifier un capteur
class CapteurForm(forms.ModelForm):

    class Meta:
        model = Capteur

        fields = [
            "nom",
            "type_capteur",
            "emplacement",
            "actif",
            "description"
        ]

        labels = {
            "nom": "Nom du capteur",
            "type_capteur": "Type de capteur",
            "emplacement": "Emplacement",
            "actif": "Capteur actif",
            "description": "Description"
        }