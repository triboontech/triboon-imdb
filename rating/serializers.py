from rest_framework import serializers
from rating.models import Rating
from movie.models import Movie

class RatingSerializer(serializers.ModelSerializer):
    movie = serializers.SlugRelatedField(
        slug_field="title",
        queryset=Movie.objects.all(),
        write_only=True,
    )
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Rating
        fields = [
            "id",
            "user",
            "movie",
            "score",
            "comment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "user", "movie", "created_at"
        ]
