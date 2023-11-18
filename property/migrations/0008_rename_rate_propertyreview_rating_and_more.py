# Generated by Django 4.2.4 on 2023-11-18 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_propertyreview_ip_propertyreview_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyreview',
            old_name='rate',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='propertyreview',
            old_name='feedback',
            new_name='review',
        ),
        migrations.AddField(
            model_name='propertyreview',
            name='subject',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
