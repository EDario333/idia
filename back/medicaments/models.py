# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext

from catalogues.models import \
MyModelWithDescriptionNotesComments

from cfg import app

class Medicament(MyModelWithDescriptionNotesComments):
	name_es=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Medicament model","Name"), unique=True,\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	name_en=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Medicament model","Name"), unique=True,\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	class Meta:
		verbose_name = pgettext("Medicament model", "Medicament")
		verbose_name_plural = pgettext("Medicament model", "Medicaments")