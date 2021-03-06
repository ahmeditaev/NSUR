# Generated by Django 2.0.3 on 2018-03-29 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0046_auto_20180329_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 9, 26, 30, 457732, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='photomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 9, 26, 30, 459333, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 9, 26, 30, 458892, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='videomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 9, 26, 30, 459749, tzinfo=utc)),
        ),
    ]
