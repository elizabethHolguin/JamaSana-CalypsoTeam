# Generated by Django 3.1.3 on 2021-03-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='nombre_perfil',
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
