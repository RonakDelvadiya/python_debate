# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtapp', '0002_auto_20180208_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
