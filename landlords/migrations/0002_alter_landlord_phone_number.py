# Generated by Django 4.2.3 on 2023-08-07 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlord',
            name='phone_number',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "070xxxxxxxx". 11 digits allowed.', regex='^\\d{11}$')]),
        ),
    ]
