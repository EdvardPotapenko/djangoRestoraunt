# Generated by Django 3.1.5 on 2021-01-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteApp', '0004_auto_20210130_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
