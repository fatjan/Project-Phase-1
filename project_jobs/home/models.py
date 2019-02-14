from django.db import models


class user(models.Model):
    username = models.CharField(max_length = 255)
    nama = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    dokumen = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.username