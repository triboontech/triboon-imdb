from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from director.models import Director
from director.serializers import DirectorSerializer

class DirectorViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
