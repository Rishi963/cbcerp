# Generated by Django 4.0.3 on 2023-07-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_data_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreg',
            name='studend_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
