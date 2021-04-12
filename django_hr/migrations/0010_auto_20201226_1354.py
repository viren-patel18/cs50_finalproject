# Generated by Django 3.0.8 on 2020-12-26 18:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0009_leaverequest_leavetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='content',
            field=models.CharField(default='content', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='django_hr.Employee'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='timestamp',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='announcement',
            name='title',
            field=models.CharField(default='title', max_length=100),
            preserve_default=False,
        ),
    ]