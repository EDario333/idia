# Generated by Django 2.2.13 on 2020-06-14 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axis', '0004_auto_20200614_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axis',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 6, 14, 10, 9, 26, 772001), editable=False),
        ),
        migrations.AlterField(
            model_name='axis',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 10, 9, 26, 772029), editable=False),
        ),
    ]
