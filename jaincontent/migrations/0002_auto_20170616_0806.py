# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-16 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jaincontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='type',
            field=models.CharField(blank=True, choices=[(b'list', b'list'), (b'News', b'News'), (b'content_list', b'content_list'), (b'gallery', b'gallery'), (b'video', b'video')], max_length=20, null=True),
        ),
    ]
