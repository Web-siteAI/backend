# Generated by Django 2.1.5 on 2019-03-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_page_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_name_en',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
