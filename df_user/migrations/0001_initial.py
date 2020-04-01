# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uname', models.CharField(verbose_name='用户名', max_length=20)),
                ('upwd', models.CharField(verbose_name='密码', max_length=40)),
                ('uemail', models.CharField(verbose_name='电子邮箱', max_length=30)),
                ('ushow', models.CharField(verbose_name='收件人名字', max_length=20, default='')),
                ('uaddress', models.CharField(verbose_name='收件地址', max_length=100, default='')),
                ('uyoubian', models.CharField(verbose_name='收件邮编', max_length=6, default='')),
                ('uphone', models.CharField(verbose_name='收件人电话', max_length=11, default='')),
            ],
            options={
                'verbose_name_plural': '用户管理',
            },
        ),
    ]
