# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArenaDraftStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snapshot_time', models.DateTimeField()),
                ('wins', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
                ('deck_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BrawlSeasonStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snapshot_time', models.DateTimeField()),
                ('season', models.IntegerField()),
                ('brawl', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('played', models.PositiveIntegerField()),
                ('streak', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snapshot_time', models.DateTimeField()),
                ('gold_progress', models.PositiveIntegerField()),
                ('gold_balance', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RankedSeasonStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snapshot_time', models.DateTimeField()),
                ('wild', models.BooleanField()),
                ('season', models.IntegerField()),
                ('rank', models.PositiveIntegerField()),
                ('stars', models.PositiveIntegerField()),
                ('best_stars', models.PositiveIntegerField()),
                ('wins', models.PositiveIntegerField()),
                ('streak', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StatsMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hearthstone_build', models.PositiveIntegerField()),
                ('platform', models.PositiveIntegerField(default=1)),
                ('battlenet_id', models.BigIntegerField()),
                ('region', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='rankedseasonstats',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.StatsMeta'),
        ),
        migrations.AddField(
            model_name='playerstats',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.StatsMeta'),
        ),
        migrations.AddField(
            model_name='brawlseasonstats',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.StatsMeta'),
        ),
        migrations.AddField(
            model_name='arenadraftstats',
            name='meta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.StatsMeta'),
        ),
    ]
