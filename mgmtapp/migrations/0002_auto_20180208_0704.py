# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mgmtapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='creater',
        ),
        migrations.AddField(
            model_name='discussion',
            name='creater_id',
            field=models.ForeignKey(related_name=b'Dis_Creater', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
