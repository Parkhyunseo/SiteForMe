# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='content_color',
            field=models.CharField(choices=[('red', 'red'), ('pink', 'pink'), ('purple', 'purple'), ('deep-purple', 'depp-purple'), ('indigo', 'indigo'), ('blue', 'blue'), ('light-blue', 'light-blue'), ('cyan', 'cyan'), ('teal', 'teal'), ('green', 'green'), ('light-green', 'light-green'), ('lime', 'lime'), ('yellow', 'yellow'), ('amber', 'amber'), ('orange', 'orange'), ('depp-orange', 'deep-orange'), ('brown', 'brown'), ('blue-grey', 'blue-grey')], default='teal', max_length=20),
        ),
    ]
