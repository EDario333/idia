# Generated by Django 2.2.13 on 2020-06-14 09:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GravitySpecifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(default=datetime.datetime(2020, 6, 14, 9, 45, 40, 180706), editable=False)),
                ('created_when', models.DateField(default=datetime.datetime(2020, 6, 14, 9, 45, 40, 180741), editable=False)),
                ('disabled', models.BooleanField(default=False, editable=False)),
                ('disabled_at', models.TimeField(blank=True, default=None, editable=False, null=True)),
                ('disabled_when', models.DateField(blank=True, default=None, editable=False, null=True)),
                ('disabled_reason', models.CharField(blank=True, default=None, editable=False, max_length=1024, null=True, verbose_name='Specify the reason to disable this product')),
                ('dropped', models.BooleanField(default=False, editable=False)),
                ('dropped_at', models.TimeField(blank=True, default=None, editable=False, null=True)),
                ('dropped_when', models.DateField(blank=True, default=None, editable=False, null=True)),
                ('dropped_reason', models.CharField(blank=True, default=None, editable=False, max_length=1024, null=True, verbose_name='Specify the reason to drop this object')),
                ('description_es', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Description')),
                ('notes_es', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Notes')),
                ('comments_es', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Comments')),
                ('description_en', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Description')),
                ('notes_en', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Notes')),
                ('comments_en', models.TextField(blank=True, default=None, max_length=1024, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(1024)], verbose_name='Comments')),
                ('name_es', models.CharField(default=None, max_length=254, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(254)], verbose_name='Name')),
                ('name_en', models.CharField(default=None, max_length=254, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(254)], verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Gravity specifier',
                'verbose_name_plural': 'Gravity specifiers',
            },
        ),
    ]
