# Generated by Django 5.1.3 on 2024-11-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_potentialclient_unique_field_combination'),
    ]

    operations = [
        migrations.AddField(
            model_name='potentialclient',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=4000),
        ),
    ]