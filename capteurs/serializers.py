from rest_framework.serializers import ModelSerializer
from .models import Capteur


class CapteurSerializer(ModelSerializer):

    class Meta:
        model = Capteur
        fields = [
            'id',
            'nom',
            'type_capteur',
            'emplacement',
            'actif',
            'description'
        ]