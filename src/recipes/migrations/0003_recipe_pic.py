# Generated by Django 4.2.16 on 2024-11-11 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_cooking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_image.png', upload_to='recipes'),
        ),
    ]
