# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogtest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='blogtest.Category', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, default=datetime.datetime(2015, 11, 27, 14, 58, 45, 428365, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
