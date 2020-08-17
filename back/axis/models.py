# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext
# from django.utils.translation import gettext as _

from catalogues.models import \
MyModelWithDescriptionNotesComments

class Axis(MyModelWithDescriptionNotesComments):
	name_es=models.CharField(\
		max_length=100, default=None, blank=False, null=False,\
		verbose_name=pgettext("Axis model","Name"), unique=True,\
		validators=[MinLengthValidator(2),MaxLengthValidator(100)])

	name_en=models.CharField(\
		max_length=100, default=None, blank=False, null=False,\
		verbose_name=pgettext("Axis model","Name"), unique=True,\
		validators=[MinLengthValidator(2),MaxLengthValidator(100)])

	class Meta:
		verbose_name = pgettext("Axis model", "Axis")
		verbose_name_plural = pgettext("Axis model", "Axises")