# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-15 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_case', '0002_auto_20180812_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttaskinfo',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='discovertime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发现时间'),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='enterpriseinvoledname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='企业关键字'),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='status',
            field=models.FloatField(blank=True, null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='ttaskinfo',
            name='taskid',
            field=models.CharField(max_length=20, verbose_name='任务号'),
        ),
    ]
