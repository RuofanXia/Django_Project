# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import scgarden.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('scgarden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegallery',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date(2014, 11, 15), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagecontent',
            name='images',
            field=stdimage.models.StdImageField(upload_to=scgarden.models.get_upload_file_name, blank=True),
        ),
    ]
