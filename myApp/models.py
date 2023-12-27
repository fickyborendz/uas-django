from django.db import models

# Create your models here.
class kelompok(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField()

    def _str_(self):
        return self.nama
    
class bukuu(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(kelompok, on_delete=models.CASCADE, null=True)
    
    def _str_(self):
        return self.judul