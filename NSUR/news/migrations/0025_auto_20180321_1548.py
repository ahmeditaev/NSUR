# Generated by Django 2.0.3 on 2018-03-21 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0024_auto_20180321_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 21, 9, 48, 27, 926948, tzinfo=utc), null=True),
        ),
    ]