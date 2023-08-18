from django.db import models


# Create your models here.

class Film(models.Model):
    f_name = models.CharField(max_length=250)
    f_year = models.CharField(max_length=250)
    f_genre = models.CharField(max_length=250)
    f_prate = models.CharField(max_length=250)
    f_cast = models.CharField(max_length=250)
    f_dir = models.CharField(max_length=250)
    f_plot = models.TextField()
    f_img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.f_name
