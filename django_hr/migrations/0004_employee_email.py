# Generated by Django 3.0.8 on 2020-12-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0003_auto_20201220_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='admin@django_hr.ca', max_length=30),
            preserve_default=False,
        ),
    ]
