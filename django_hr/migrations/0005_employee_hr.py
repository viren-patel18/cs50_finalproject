# Generated by Django 3.0.8 on 2020-12-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0004_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hr',
            field=models.BooleanField(default=False),
        ),
    ]