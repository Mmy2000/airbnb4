# Generated by Django 4.2.4 on 2023-09-08 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_newslitter_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslitter',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 8, 0, 6, 50, 83553, tzinfo=datetime.timezone.utc)),
        ),
    ]