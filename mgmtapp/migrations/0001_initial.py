# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=255, verbose_name=b'Text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('creater', models.ForeignKey(related_name=b'Comm_Creater', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('text', models.TextField(verbose_name=b'Text')),
                ('discussion_type', models.CharField(max_length=10, verbose_name=b'Type', choices=[(b'article', b'Article'), (b'question', b'Question'), (b'post', b'Post'), (b'blog', b'Blog')])),
                ('is_published', models.BooleanField(default=True, verbose_name=b'Is published')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(max_length=255, upload_to=b'media/')),
                ('added_by', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('creater', models.ForeignKey(related_name=b'Dis_Creater', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='discussion',
            field=models.ForeignKey(to='mgmtapp.Discussion'),
            preserve_default=True,
        ),
    ]
