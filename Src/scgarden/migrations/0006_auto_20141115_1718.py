# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import scgarden.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('scgarden', '0005_auto_20141115_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecontent',
            name='imageGallery',
        ),
        migrations.DeleteModel(
            name='ImageContent',
        ),
        migrations.AddField(
            model_name='imagegallery',
            name='images',
            field=stdimage.models.StdImageField(default=datetime.date(2014, 11, 15), upload_to=scgarden.models.get_upload_file_name, blank=True),
            preserve_default=False,
        ),
    ]
