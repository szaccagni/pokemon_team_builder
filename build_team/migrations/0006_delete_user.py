# Generated by Django 4.0.1 on 2022-05-06 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0005_remove_team_p1_id_remove_team_p2_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]