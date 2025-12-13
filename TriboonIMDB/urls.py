
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from movie import views as movie_views
from director import views as director_views
from rating import views as rating_views

router=routers.DefaultRouter()
router.register('movies',movie_views.MovieViewSet)
router.register('directors',director_views.DirectorViewSet)
router.register('ratings',rating_views.RatingViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
