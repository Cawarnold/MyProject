# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150427_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('reg_date', models.DateTimeField(default=datetime.datetime(2015, 4, 27, 16, 52, 30, 165000, tzinfo=utc), verbose_name=b'registry date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 16, 52, 30, 164000, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=True,
        ),
    ]
