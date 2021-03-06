# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditableBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('slug', models.SlugField(max_length=255, verbose_name='\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0438\u043c\u044f')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442')),
                ('enabled', models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0435\u043d')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0439 \u0431\u043b\u043e\u043a',
                'verbose_name_plural': '\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u0443\u0435\u043c\u044b\u0435 \u0431\u043b\u043e\u043a\u0438',
            },
        ),
    ]
