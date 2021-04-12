# Generated by Django 3.0.8 on 2021-01-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0013_checkin_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('PENDING APPROVAL', 'Pending Approval'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected')], max_length=30),
        ),
    ]
