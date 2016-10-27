# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuento', '0002_capitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulo',
            name='docfile',
            field=models.ImageField(default='none', upload_to=''),
        ),
    ]
