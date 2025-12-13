from rest_framework import serializers
from director.models import Director

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            'id',
            'name',
            'birth_date'
        ]
