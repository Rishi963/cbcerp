# Generated by Django 4.0.3 on 2023-07-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=500)),
                ('father_occupation', models.CharField(max_length=500)),
                ('mother_name', models.CharField(max_length=500)),
                ('mother_occupation', models.CharField(max_length=500)),
                ('nationality', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=500)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('board', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
                ('mark_10', models.CharField(max_length=100)),
                ('mark_11', models.CharField(max_length=100)),
                ('mark_12', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('batch', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('total_fee', models.CharField(max_length=100)),
                ('join_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('scholorship', models.CharField(max_length=100)),
                ('scholorship_percentage', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('about_studibreeze', models.CharField(max_length=100)),
            ],
        ),
    ]
