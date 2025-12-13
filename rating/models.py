from django.db import models
from movie.models import Movie
from django.contrib.auth.models import User

from movie.models import *

class Rating(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='ratings',
        verbose_name='فیلم'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews", verbose_name="کاربر"
    )
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    comment = models.TextField(blank=True, null=True, verbose_name="نظر")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین ویرایش")

    def __str__(self):
        return f"{self.movie.title} — {self.score} از ۱۰"
