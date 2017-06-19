from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone

import django.contrib.postgres.fields.jsonb
import json

def tranfer_data(apps, schema_editor):
	Notification = apps.get_model("notifications", "notification")
	db_alias = schema_editor.connection.alias
	nn = Notification.objects.using(db_alias).all()
	for n in nn:
		if n.data:
			j = json.loads(n.data)
			n.data2 = j
			n.save()


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20160504_1520'),
    ]

    operations = [
    	migrations.AddField(
            model_name='notification',
            name='data2',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True, blank=True),
        ),
        migrations.RunPython(tranfer_data),
        migrations.RemoveField(
            model_name='notification',
            name='data',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='data2',
            new_name='data',
        ),

    ]