# Generated by Django 5.0.6 on 2024-07-10 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_userbankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]