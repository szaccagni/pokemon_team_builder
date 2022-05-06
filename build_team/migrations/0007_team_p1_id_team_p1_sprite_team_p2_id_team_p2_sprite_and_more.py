# Generated by Django 4.0.1 on 2022-05-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_team', '0006_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='p1_id',
            field=models.CharField(default='25', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='p1_sprite',
            field=models.CharField(default='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='p2_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p2_sprite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p3_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p3_sprite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p4_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p4_sprite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p5_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p5_sprite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p6_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='team',
            name='p6_sprite',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='p2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='p3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='p4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='p5',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='p6',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
