# Generated by Django 2.1.7 on 2019-02-14 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
