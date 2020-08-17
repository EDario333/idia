# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext

from catalogues.models import \
MyModelWithDescriptionNotesComments

from medicaments.models import Medicament

from cfg import app

class Treatment(MyModelWithDescriptionNotesComments):
	name_es=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Treatment model","Name"), unique=True,\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	name_en=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Treatment model","Name"), unique=True,\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	medicaments=models.ManyToManyField(Medicament)

	class Meta:
		verbose_name = pgettext("Treatment model", "Treatment")
		verbose_name_plural = pgettext("Treatment model", "Treatments")