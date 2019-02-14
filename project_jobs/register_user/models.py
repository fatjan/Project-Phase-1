from django.db import models


class User(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 100)
    nama = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    dokumen = models.FileField(upload_to='static/')


    def __str__(self):
        return self.username