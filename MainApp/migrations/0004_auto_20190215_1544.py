# Generated by Django 2.1.5 on 2019-02-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_auto_20190215_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='site_url',
            field=models.URLField(max_length=255, verbose_name='site_url'),
        ),
    ]
