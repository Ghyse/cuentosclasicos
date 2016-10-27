# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuento', '0003_capitulo_docfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitulo',
            old_name='docfile',
            new_name='img',
        ),
    ]
