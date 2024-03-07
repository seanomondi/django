from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=25, blank=False)
    id_no = models.IntegerField(blank=False)
    phone = models.IntegerField(blank=False)
    email = models.EmailField(blank=False)
    project = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='profiles', blank=False)

    def __str__(self):
        return self.name
