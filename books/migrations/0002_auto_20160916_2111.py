# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(related_name='books', blank=True, to='books.Category', null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=250, blank=True),
        ),
    ]
