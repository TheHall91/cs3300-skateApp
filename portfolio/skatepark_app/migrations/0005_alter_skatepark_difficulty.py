# Generated by Django 4.2 on 2024-04-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skatepark_app', '0004_rename_location_skatepark_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skatepark',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'), ('Extreme', 'Extreme')], max_length=200),
        ),
    ]
