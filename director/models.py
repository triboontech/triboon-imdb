from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100,verbose_name='کارگردان')
    birth_date = models.DateField()
    def __str__(self):
        return self.name
