# Generated by Django 2.2.13 on 2020-06-14 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0003_auto_20200614_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaddress',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 218975), editable=False),
        ),
        migrations.AlterField(
            model_name='personaddress',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 219004), editable=False),
        ),
        migrations.AlterField(
            model_name='personemail',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 218975), editable=False),
        ),
        migrations.AlterField(
            model_name='personemail',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 219004), editable=False),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 218975), editable=False),
        ),
        migrations.AlterField(
            model_name='personphone',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 219004), editable=False),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 218975), editable=False),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='created_when',
            field=models.DateField(default=datetime.datetime(2020, 6, 14, 9, 48, 58, 219004), editable=False),
        ),
    ]
