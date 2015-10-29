# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ablum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='basic.Person')),
                ('instrument', models.CharField(max_length=100)),
            ],
            bases=('basic.person',),
        ),
        migrations.AddField(
            model_name='ablum',
            name='artist',
            field=models.ForeignKey(to='basic.Musician'),
        ),
    ]
