# Generated by Django 2.0.3 on 2018-03-29 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0038_auto_20180322_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField()),
                ('twitter', models.TextField()),
                ('vk', models.TextField()),
                ('pinterest', models.TextField()),
                ('tubmlr', models.TextField()),
                ('dribbble', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 36, 29, 371480, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='photomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 36, 29, 373057, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 36, 29, 372602, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='videomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 36, 29, 373476, tzinfo=utc)),
        ),
    ]
