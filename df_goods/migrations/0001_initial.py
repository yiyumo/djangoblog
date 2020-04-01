# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('gtitle', models.CharField(verbose_name='名字', max_length=20)),
                ('gpic', models.ImageField(verbose_name='图片', upload_to='df_goods')),
                ('gprice', models.DecimalField(verbose_name='价钱', max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(verbose_name='单位', max_length=20, default='500g')),
                ('gclick', models.IntegerField(verbose_name='点击')),
                ('gjianjie', models.CharField(max_length=200)),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', tinymce.models.HTMLField(verbose_name='描述')),
            ],
            options={
                'verbose_name_plural': '水果',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ttitle', models.CharField(verbose_name='种类', max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '水果类型修改',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
