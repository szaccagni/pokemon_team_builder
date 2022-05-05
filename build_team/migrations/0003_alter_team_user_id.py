# Generated by Django 4.0.1 on 2022-05-05 01:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
