# Generated by Django 5.0.6 on 2024-05-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_provider_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='price',
            field=models.FloatField(),
        ),
    ]
