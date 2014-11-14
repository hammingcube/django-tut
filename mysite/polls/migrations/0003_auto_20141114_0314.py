# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(default=1, to='polls.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
