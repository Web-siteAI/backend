# Generated by Django 2.1.5 on 2019-02-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20190209_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='site_url',
            field=models.URLField(default='', max_length=255, verbose_name='site_en'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='social_net',
            field=models.CharField(default='', max_length=255, verbose_name='social_net'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='social_net_url',
            field=models.URLField(default='', max_length=255, verbose_name='social_net_url'),
            preserve_default=False,
        ),
    ]
