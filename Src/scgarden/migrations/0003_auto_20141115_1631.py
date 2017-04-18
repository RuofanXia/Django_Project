# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import scgarden.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('scgarden', '0002_auto_20141115_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecontent',
            name='images',
            field=stdimage.models.StdImageField(upload_to=scgarden.models.get_upload_file_name, blank=True),
        ),
    ]
