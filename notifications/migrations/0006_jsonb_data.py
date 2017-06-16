# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone
import django.contrib.postgres.fields.jsonb
import json

def forwards_func(apps, schema_editor):
    Notification = apps.get_model("notifications", "notification")
    db_alias = schema_editor.connection.alias
    nn = Notification.objects.using(db_alias).all()
    for n in nn:
        j = json.loads(n.data)
        n.data = j
        n.save()

class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, blank=True),
            preserve_default=True
        ),
        migrations.RunPython(forwards_func),
    ]
