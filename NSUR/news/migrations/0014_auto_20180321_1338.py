# Generated by Django 2.0.3 on 2018-03-21 07:38

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20180319_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 3, 21, 7, 38, 47, 685204, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=''),
        ),
    ]
