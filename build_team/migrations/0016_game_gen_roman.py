# Generated by Django 4.0.1 on 2022-06-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0015_game_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='gen_roman',
            field=models.CharField(default='i', max_length=255),
            preserve_default=False,
        ),
    ]
