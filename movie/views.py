from django.db.models import Avg, Count
from rest_framework.viewsets import ModelViewSet
from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().annotate(
        average_rating=Avg('ratings__score'),
        rating_count=Count('ratings')
    )
    serializer_class = MovieSerializer
