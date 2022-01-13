# Generated by Django 3.2 on 2022-01-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_car_car_premium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='tour_rating',
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_ranking',
            field=models.DecimalField(decimal_places=1, default=5.0, max_digits=2),
            preserve_default=False,
        ),
    ]
