# Generated by Django 5.1.3 on 2024-11-26 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_alter_contract_documentation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='documentation',
            field=models.FileField(blank=True, null=True, upload_to='contracts/documentations/'),
        ),
    ]
