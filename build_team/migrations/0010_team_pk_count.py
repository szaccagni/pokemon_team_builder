# Generated by Django 4.0.1 on 2022-05-13 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0009_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='pk_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
