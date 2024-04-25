# Generated by Django 4.2 on 2024-04-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatepark_app', '0008_remove_review_park_review_skatepark'),
    ]

    operations = [
        migrations.AddField(
            model_name='skatepark',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='skatepark',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]