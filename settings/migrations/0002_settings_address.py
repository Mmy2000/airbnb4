# Generated by Django 4.2.4 on 2023-08-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='address',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
