from django.db import models
from django.db.models.fields import TextField

# Create your models here.
class kelamin(models.Model):
    name = models.TextField(default='')

class ortu(models.Model):
    name = models.TextField(default='')

class anak(models.Model):
    nama = models.TextField(default='')
    jenis_kelamin = models.ForeignKey(kelamin, on_delete=models.CASCADE)
    nama_orang_tua = models.ForeignKey(ortu, on_delete=models.CASCADE)