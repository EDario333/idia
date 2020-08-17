# Generated by Django 2.2.13 on 2020-07-21 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicaments', '0002_medicament_created_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 7, 21, 23, 28, 4, 145955), editable=False),
        ),
        migrations.AlterField(
            model_name='medicament',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 7, 21, 23, 28, 4, 146001), editable=False),
        ),
    ]
