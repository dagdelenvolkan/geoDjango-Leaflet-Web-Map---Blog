from django.contrib.gis.db import models

# Create your models here.

class Saglik(models.Model):
    ILCE_ADI = models.CharField(max_length=200)
    ADI= models.CharField(max_length=200)
    ALT_KATEGORI= models.CharField(max_length=200)
    ADRES= models.CharField(max_length=400)
    TELEFON= models.CharField(max_length=200)
    WEBSITESI = models.CharField(max_length=200)
    ACIL_SERVIS = models.CharField(max_length=200)
    YATAK  =  models.IntegerField(null=True)
    AMBULANS = models.CharField(max_length=200)
    MAHALLE = models.CharField(max_length=200)
    POINT = models.GeometryField()
    
    
    def __str__(self):
        return self.ADI