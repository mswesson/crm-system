# Generated by Django 5.1.3 on 2024-11-20 08:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_potentialclient_next_interaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potentialclient',
            name='next_interaction_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
