# Generated by Django 2.0.6 on 2018-09-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_auto_20180915_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='criacao',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='ultima_alteracao',
            field=models.DateField(auto_now=True),
        ),
    ]
