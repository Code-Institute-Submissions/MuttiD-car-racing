# Generated by Django 3.2.17 on 2023-05-04 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0004_auto_20230503_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carreview',
            old_name='feature_image',
            new_name='featured_image',
        ),
    ]