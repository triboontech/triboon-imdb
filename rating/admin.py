from django.contrib import admin

from rating.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie','score']
    list_filter = ['score', 'movie__genre']
    search_fields = ['movie__title']
    readonly_fields = ['score',]
