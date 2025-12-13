from rest_framework import serializers
from movie.models import Movie
from director.models import Director


class MovieSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True, default=None, allow_null=True)
    director = serializers.SlugRelatedField(
         slug_field='name',
         queryset=Director.objects.all()
    )

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'release_date',
            'genre',
            'director',
            'average_rating'
        ]
