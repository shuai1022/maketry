# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='try_carousel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('img_url', models.CharField(max_length=256)),
                ('link_url', models.CharField(max_length=256)),
                ('sort', models.IntegerField(default=0)),
                ('type', models.IntegerField(default=0)),
                ('state', models.IntegerField(default=0)),
                ('createdate', models.DateTimeField(default=datetime.datetime(2016, 1, 20, 8, 55, 39, 344000, tzinfo=utc))),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2016, 1, 20, 8, 55, 39, 344000, tzinfo=utc))),
            ],
        ),
    ]
