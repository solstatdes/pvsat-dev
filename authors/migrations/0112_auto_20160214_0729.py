# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import authors.models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0111_auto_20160214_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstract',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 14, 7, 29, 6, 361078)),
        ),
        migrations.AlterField(
            model_name='abstract',
            name='paper',
            field=models.FileField(null=True, upload_to=b'abstract_uploads', validators=[authors.models.validate_file_extension]),
        ),
    ]
