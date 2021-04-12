# Generated by Django 3.0.8 on 2020-12-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0002_auto_20201220_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postalCode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='province',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
