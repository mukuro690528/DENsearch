# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-12 06:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_WOM', models.IntegerField(default=0)),
                ('score_ec', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_ec', models.IntegerField(default=0)),
                ('score_tem', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_tem', models.IntegerField(default=0)),
                ('score_con', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_con', models.IntegerField(default=0)),
                ('score_soc', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_soc', models.IntegerField(default=0)),
                ('score_qua', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_qua', models.IntegerField(default=0)),
                ('score_oth', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('count_oth', models.IntegerField(default=0)),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_detail', to='recommendation.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='WordScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=3, max_digits=4)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
    ]
