from django.db import models
from django.utils import timezone
from django.shortcuts import render


class Post(models.Model):
    yazar = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilis_tarihi = models.DateTimeField(
            default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self. yayinlama_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik