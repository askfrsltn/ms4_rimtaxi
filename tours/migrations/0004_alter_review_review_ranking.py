# Generated by Django 3.2 on 2022-01-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_alter_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_ranking',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
