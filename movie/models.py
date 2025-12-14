from django.db import models
from director.models import Director

class Movie(models.Model):
    GENRE_CHOICES = (
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('Documentary', 'Documentary'),
        ('Animation', 'Animation'),
        ('Fantasy', 'Fantasy'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=200,verbose_name='فیلم')
    release_date = models.DateField(verbose_name="تاریخ انتشار")
    genre = models.CharField(max_length=100,choices=GENRE_CHOICES,verbose_name="دسته بندی")
    director = models.ForeignKey('director.Director', on_delete=models.CASCADE,verbose_name="کارگردان")
    duration = models.PositiveIntegerField(null=True, blank=True, verbose_name="مدت زمان")


    def __str__(self):
        return self.title
