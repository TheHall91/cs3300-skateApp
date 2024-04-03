# Generated by Django 4.2 on 2024-04-01 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skatepark_app', '0002_alter_skatepark_location_alter_skatepark_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skatepark',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Easy'), ('3', 'Medium'), ('4', 'Hard'), ('5', 'Extreme')], max_length=200),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Review Title:')),
                ('review', models.CharField(max_length=400, verbose_name='Review:')),
                ('park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skatepark_app.skatepark')),
            ],
        ),
    ]
