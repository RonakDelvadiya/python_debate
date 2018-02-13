# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtapp', '0004_auto_20180209_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='added_by',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
