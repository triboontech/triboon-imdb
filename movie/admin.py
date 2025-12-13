from django.contrib import admin

from movie.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','director','genre', 'release_date', )
    list_filter = ('genre',)
    search_fields = ('title',)
    ordering = ('-release_date',)
