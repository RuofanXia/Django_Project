# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pageModule_text', models.CharField(max_length=200)),
                ('url_text', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
