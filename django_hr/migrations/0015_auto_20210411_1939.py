# Generated by Django 3.0.8 on 2021-04-11 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_hr', '0014_auto_20210103_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='status',
            field=models.CharField(choices=[('P', 'Pending Approval'), ('A', 'Approved'), ('R', 'Rejected')], max_length=30),
        ),
    ]
