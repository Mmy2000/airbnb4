# Generated by Django 4.2.4 on 2023-11-18 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_rename_rate_propertyreview_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyreview',
            old_name='auther',
            new_name='user',
        ),
    ]
