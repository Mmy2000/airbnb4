# Generated by Django 4.2.4 on 2023-11-18 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_alter_newslitter_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslitter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 18, 21, 20, 4, 946783, tzinfo=datetime.timezone.utc)),
        ),
    ]