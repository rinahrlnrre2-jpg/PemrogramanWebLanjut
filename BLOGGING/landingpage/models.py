from django.db import models


class Kategori(models.Model):

    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
    
class Artikel(models.Model):

    judul = models.CharField(max_length=200)

    konten = models.TextField()

    kategori = models.ForeignKey(
        Kategori,
        on_delete=models.CASCADE
    )

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.judul