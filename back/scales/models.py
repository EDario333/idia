# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext

from catalogues.models import \
MyModelWithDescriptionNotesComments

class Scale(MyModelWithDescriptionNotesComments):
	code=models.CharField(\
		max_length=4, default=None, blank=False, null=False,\
		verbose_name=pgettext("Scales model","Code"),\
		validators=[MinLengthValidator(2),MaxLengthValidator(4)])

	def __str__(self):
		return self.description_es

	class Meta:
		verbose_name = pgettext("Scales model", "Scale")
		verbose_name_plural = pgettext("Scales model", "Scales")