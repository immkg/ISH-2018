# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_id', models.IntegerField()),
                ('label', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images')),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PLotBuildingconnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morags.Building')),
                ('parking_lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='morags.ParkingLot')),
            ],
        ),
    ]
