# Generated by Django 3.1.3 on 2021-03-04 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0002_auto_20210304_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='user',
            field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
