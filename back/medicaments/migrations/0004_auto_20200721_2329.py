# Generated by Django 2.2.13 on 2020-07-21 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0003_auto_20200721_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 7, 21, 23, 29, 11, 517956), editable=False),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 7, 21, 23, 29, 11, 517998), editable=False),
        ),
    ]
