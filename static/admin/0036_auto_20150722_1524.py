# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0035_auto_20150721_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 15, 24, 36, 839371)),
        ),
    ]
