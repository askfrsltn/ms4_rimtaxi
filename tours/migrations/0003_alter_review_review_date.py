# Generated by Django 3.2 on 2022-01-13 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20220113_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.CharField(max_length=24),
        ),
    ]
