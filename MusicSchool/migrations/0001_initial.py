# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-03-25 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=255)),
                ('Hours', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=255)),
                ('Snname', models.CharField(max_length=255)),
                ('Age', models.IntegerField(default=0)),
                ('Ssex', models.CharField(max_length=255)),
                ('Pnum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Learnday', models.CharField(max_length=255)),
                ('Learnhour', models.CharField(max_length=255)),
                ('Level', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicSchool.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicSchool.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teachday', models.CharField(max_length=255)),
                ('Teachhour', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicSchool.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tname', models.CharField(max_length=255)),
                ('Tnname', models.CharField(max_length=255)),
                ('Tsex', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='teach',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicSchool.Teacher'),
        ),
    ]
