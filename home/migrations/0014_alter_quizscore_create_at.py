# Generated by Django 5.1 on 2024-08-10 15:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_quizscore_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizscore',
            name='create_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]