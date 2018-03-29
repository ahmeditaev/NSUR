# Generated by Django 2.0.3 on 2018-03-29 08:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0040_auto_20180329_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dribble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pinterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Tumblr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='SocialMedia',
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 53, 52, 353005, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='photomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 53, 52, 354991, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pressclipping',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 29, 8, 53, 52, 354316, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='videomediabox',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 29, 8, 53, 52, 355467, tzinfo=utc)),
        ),
    ]
