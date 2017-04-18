# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import scgarden.models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('images', stdimage.models.StdImageField(upload_to=scgarden.models.get_upload_file_name, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image_text', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagecontent',
            name='imageGallery',
            field=models.ForeignKey(to='scgarden.ImageGallery'),
            preserve_default=True,
        ),
    ]
