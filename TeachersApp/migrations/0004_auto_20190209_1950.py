# Generated by Django 2.1.5 on 2019-02-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeachersApp', '0003_auto_20190209_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='academic_site',
            field=models.CharField(blank=True, max_length=255, verbose_name='academic_site'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='description_en',
            field=models.TextField(blank=True, verbose_name='description_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='full_name',
            field=models.CharField(help_text="Прізвище Ім'я По-батькові", max_length=255, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='full_name_en',
            field=models.CharField(help_text='Last name Name Surname', max_length=255, verbose_name='full_name_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='interests',
            field=models.TextField(blank=True, max_length=500, verbose_name='interests'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='interests_en',
            field=models.TextField(blank=True, max_length=500, verbose_name='interests_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(default='', max_length=255, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='role_en',
            field=models.CharField(default='', max_length=255, verbose_name='role_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='science_interests',
            field=models.CharField(blank=True, max_length=500, verbose_name='science_interests'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='science_interests_en',
            field=models.CharField(blank=True, max_length=500, verbose_name='science_interests_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='science_researches',
            field=models.TextField(blank=True, max_length=1000, verbose_name='science_researches'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='science_researches_en',
            field=models.TextField(blank=True, max_length=1000, verbose_name='science_researches_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='scientific_rank',
            field=models.CharField(default='', max_length=255, verbose_name='scientific_rank'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='scientific_rank_en',
            field=models.CharField(default=' ', max_length=255, verbose_name='scientific_rank_en'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='scopus_citations',
            field=models.IntegerField(default='0', verbose_name='scopus_citations'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='scopus_documents',
            field=models.IntegerField(default='0', verbose_name='scopus_documents'),
        ),
    ]
