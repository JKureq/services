# Generated by Django 4.1.4 on 2023-02-27 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0014_service_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='files',
            new_name='images',
        ),
    ]