# Generated by Django 2.0.3 on 2018-03-29 08:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0039_auto_20180329_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 38, 4, 389184, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='photomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 38, 4, 390750, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 38, 4, 390319, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='dribbble',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='facebook',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='pinterest',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='tubmlr',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='twitter',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='socialmedia',
            name='vk',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='videomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 38, 4, 391168, tzinfo=utc)),
        ),
    ]
