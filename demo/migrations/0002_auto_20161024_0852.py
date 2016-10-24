# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, serialize=False, primary_key=True),
        ),
    ]
