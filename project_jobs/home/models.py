from django.utils import timezone
from django.db.models import CharField, TextField, DateTimeField
from django.db import models as models

# Create your models here.
class Job(models.Model):
    job_name = models.CharField(max_length=255, default='')
    # comp_name = models.CharField(max_length=255, default='')
    lokasi = models.CharField(max_length=255, default='')
    bidang = models.CharField(max_length=255, default='')
    deadline = models.DateField(default=timezone.now)
    deskripsi = models.TextField(max_length=10000, default='')
    logo_perusahaan = models.ImageField(upload_to="Media/img")
    posted_at = models.DateTimeField(default=timezone.now)
    salary = models.IntegerField(default=3000000)

    def __str__(self):
        return self.job_name
