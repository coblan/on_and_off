# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-15 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_case', '0004_auto_20181115_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttaskinfo',
            name='accepttime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='allendtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='allimportanttime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='allmiddletime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='cancletime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='expsatisfactiontime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='feedbacktime_12345',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='firstcontacttime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='firstdispatchtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='importantsolvingtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='lastarrivetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='lastcontacttime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='lastsolvingtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='lasttakecasetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='lastupdatetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='middispatchtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='middlesolvingtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='qpdispatchtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='qplastsolvingtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='qpsolvingtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='reply_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='replytime_sl',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='synctime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
