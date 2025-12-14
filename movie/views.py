from django.db.models import Avg, Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from movie.models import Movie
from movie.pagination import MoviePagination
from movie.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all().annotate(
        average_rating=Avg('ratings__score'),
        rating_count=Count('ratings')
    )
    serializer_class = MovieSerializer
    pagination_class = MoviePagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["title", "plot"]
    ordering_fields = ["release_date", "average_rating", "rating_count"]
    ordering = ["-release_date"]
