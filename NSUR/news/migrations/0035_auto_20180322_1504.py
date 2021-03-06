# Generated by Django 2.0.3 on 2018-03-22 09:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_auto_20180322_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='photomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 9, 4, 17, 668474, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='videomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 22, 9, 4, 17, 669824, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 9, 4, 17, 666848, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 22, 9, 4, 17, 668059, tzinfo=utc), null=True),
        ),
    ]
