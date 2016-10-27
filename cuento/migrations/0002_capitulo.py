# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('texto', models.TextField()),
                ('cuento', models.ForeignKey(to='cuento.Cuento', related_name='cuentos')),
            ],
        ),
    ]
