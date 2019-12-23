# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-11-26 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToolCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='网站分类名称')),
                ('order_num', models.IntegerField(default=99, help_text='序号可以用来调整顺序，越小越靠前', verbose_name='序号')),
            ],
            options={
                'verbose_name': '工具分类',
                'verbose_name_plural': '工具分类',
                'ordering': ['order_num', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ToolLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='网站名称')),
                ('description', models.CharField(max_length=100, verbose_name='网站描述')),
                ('link', models.URLField(verbose_name='网站链接')),
                ('order_num', models.IntegerField(default=99, help_text='序号可以用来调整顺序，越小越靠前', verbose_name='序号')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tool.ToolCategory', verbose_name='网站分类')),
            ],
            options={
                'verbose_name': '推荐工具',
                'verbose_name_plural': '推荐工具',
                'ordering': ['order_num', 'id'],
            },
        ),
    ]
