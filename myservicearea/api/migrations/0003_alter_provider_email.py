# Generated by Django 5.0.6 on 2024-05-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_servicearea_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
    ]
