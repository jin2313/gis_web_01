# Generated by Django 3.2.4 on 2021-08-02 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='created_ar',
            new_name='created_at',
        ),
    ]
