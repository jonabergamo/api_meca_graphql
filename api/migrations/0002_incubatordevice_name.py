# Generated by Django 4.2.7 on 2023-12-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incubatordevice',
            name='name',
            field=models.CharField(default='Chocadeira-1', max_length=255),
        ),
    ]
