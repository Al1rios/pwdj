# Generated by Django 2.0.6 on 2018-09-15 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_auto_20180915_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='criacao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='model',
            name='ultima_alteracao',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
