# Generated by Django 2.0.3 on 2018-03-22 06:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_auto_20180322_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 6, 38, 26, 765131, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 6, 38, 26, 766396, tzinfo=utc), null=True),
        ),
    ]