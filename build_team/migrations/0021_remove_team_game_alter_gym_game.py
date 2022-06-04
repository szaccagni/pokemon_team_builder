# Generated by Django 4.0.1 on 2022-06-04 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0020_gym_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='game',
        ),
        migrations.AlterField(
            model_name='gym',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='build_team.game'),
        ),
    ]