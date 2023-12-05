# Generated by Django 4.2.7 on 2023-12-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_incubatordevice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incubatordevice',
            name='humidity_sensor',
            field=models.FloatField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='incubatordevice',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='incubatordevice',
            name='temperature_sensor',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]