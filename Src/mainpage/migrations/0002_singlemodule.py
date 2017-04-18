# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('singleModule_text', models.CharField(max_length=200)),
                ('singleModule_url_text', models.URLField()),
                ('pageModule', models.ForeignKey(to='mainpage.PageModule')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
