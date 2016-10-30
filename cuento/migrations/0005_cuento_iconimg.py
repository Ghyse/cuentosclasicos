# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuento', '0004_auto_20161027_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuento',
            name='iconImg',
            field=models.ImageField(upload_to='', default='none'),
        ),
    ]
