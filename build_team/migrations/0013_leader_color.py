# Generated by Django 4.0.1 on 2022-06-03 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0012_leader_name_location_name_reward_name_reward_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='color',
            field=models.CharField(default='FFD700', max_length=12),
            preserve_default=False,
        ),
    ]