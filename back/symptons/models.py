# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext

from catalogues.models import \
MyModelWithDescriptionNotesComments

class Sympton(MyModelWithDescriptionNotesComments):
	code=models.CharField(\
		max_length=10, default=None, blank=False, null=False,\
		verbose_name=pgettext("Sympton model","Code"),\
		validators=[MinLengthValidator(1),MaxLengthValidator(10)])

	def __str__(self):
		return self.description_es

	class Meta:
		verbose_name = pgettext("Sympton model", "Sympton")
		verbose_name_plural = pgettext("Sympton model", "Symptons")