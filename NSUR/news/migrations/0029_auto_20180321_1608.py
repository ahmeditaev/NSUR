# Generated by Django 2.0.3 on 2018-03-21 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0028_auto_20180321_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 21, 10, 8, 32, 717078, tzinfo=utc), null=True),
        ),
    ]
