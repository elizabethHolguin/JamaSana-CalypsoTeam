# Generated by Django 3.0.9 on 2021-01-19 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('paquetes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientesuscripcion',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Cliente'),
        ),
        migrations.AddField(
            model_name='clientesuscripcion',
            name='id_suscripcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paquetes.Suscripcion'),
        ),
    ]