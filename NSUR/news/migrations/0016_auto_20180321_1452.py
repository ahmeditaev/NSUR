# Generated by Django 2.0.3 on 2018-03-21 08:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_auto_20180321_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='quoteAuthor',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 21, 8, 52, 46, 859643, tzinfo=utc), null=True),
        ),
    ]
