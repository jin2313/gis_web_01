# Generated by Django 3.2.4 on 2021-08-26 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0005_auto_20210826_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='article/'),
        ),
    ]