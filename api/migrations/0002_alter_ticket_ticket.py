# Generated by Django 5.0.2 on 2024-08-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket',
            field=models.CharField(max_length=255),
        ),
    ]
