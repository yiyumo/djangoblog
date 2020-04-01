# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
        ('df_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(verbose_name='价钱', max_digits=5, decimal_places=2)),
                ('count', models.IntegerField(verbose_name='数量')),
                ('isTrue', models.BooleanField(default=False)),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
            options={
                'verbose_name_plural': '发货管理',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(primary_key=True, max_length=20, serialize=False)),
                ('odate', models.DateTimeField(verbose_name='购买日期', auto_now=True)),
                ('oIsPay', models.BooleanField(verbose_name='是否付款', default=False)),
                ('ototal', models.DecimalField(verbose_name='总价', max_digits=6, decimal_places=2)),
                ('oaddress', models.CharField(verbose_name='收货地址', max_length=150)),
                ('user', models.ForeignKey(to='df_user.UserInfo')),
            ],
            options={
                'verbose_name_plural': '订单管理',
            },
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('count', models.IntegerField(verbose_name='销量')),
                ('totalprice', models.DecimalField(verbose_name='销售额', max_digits=5, decimal_places=2)),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
            options={
                'verbose_name_plural': '销量查看',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='df_order.OrderInfo'),
        ),
    ]
