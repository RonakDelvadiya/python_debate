# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgmtapp', '0005_auto_20180209_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='creater_id',
        ),
    ]
