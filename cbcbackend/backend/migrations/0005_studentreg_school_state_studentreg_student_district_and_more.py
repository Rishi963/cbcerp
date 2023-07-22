# Generated by Django 4.0.3 on 2023-07-18 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_studentreg_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreg',
            name='school_state',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='studentreg',
            name='student_district',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='scholorship',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='scholorship_percentage',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
