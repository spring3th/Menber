# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('course_name', models.CharField(max_length=50, verbose_name='课程名')),
                ('course_subject', models.TextField(verbose_name='课程纲要')),
                ('beizhu', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '课程',
                'verbose_name': '课程',
            },
        ),
        migrations.CreateModel(
            name='Menbers',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('menber_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('menber_address', models.CharField(max_length=60, verbose_name='地址')),
                ('menber_city', models.CharField(max_length=50, verbose_name='城市')),
                ('menber_tel', models.CharField(max_length=50, verbose_name='电话')),
                ('course', models.ManyToManyField(to='menber.Courses')),
            ],
            options={
                'verbose_name_plural': '学员',
                'verbose_name': '学员',
            },
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('store_name', models.CharField(max_length=50, verbose_name='店名')),
                ('store_brand', models.CharField(max_length=50, verbose_name='品牌')),
                ('store_size', models.CharField(max_length=30, verbose_name='规模')),
                ('store_address', models.CharField(max_length=60, verbose_name='地址')),
                ('stroe_city', models.CharField(max_length=30, verbose_name='城市')),
                ('store_boss', models.CharField(max_length=30, verbose_name='老板')),
                ('store_tel', models.CharField(max_length=30, verbose_name='电话')),
            ],
            options={
                'verbose_name_plural': '店铺',
                'verbose_name': '店铺',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('teacher_name', models.CharField(max_length=30, verbose_name='姓名')),
                ('teacher_sex', models.CharField(max_length=10, verbose_name='性别')),
                ('teacher_organize', models.CharField(max_length=50, verbose_name='机构')),
                ('teacher_address', models.CharField(max_length=60, verbose_name='地址')),
                ('teacher_contact', models.CharField(max_length=30, verbose_name='联系人')),
                ('teacher_tel', models.CharField(max_length=50, verbose_name='联系电话')),
                ('beizhu', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '讲师',
                'verbose_name': '讲师',
            },
        ),
        migrations.AddField(
            model_name='menbers',
            name='menber_store',
            field=models.ForeignKey(to='menber.Stores', verbose_name='店名'),
        ),
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ManyToManyField(to='menber.Teacher'),
        ),
    ]
