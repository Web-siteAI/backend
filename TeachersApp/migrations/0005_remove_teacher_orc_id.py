# Generated by Django 2.0.3 on 2018-11-21 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TeachersApp', '0004_auto_20181121_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='orc_id',
        ),
    ]
