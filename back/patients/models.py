# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.translation import pgettext

from catalogues.models import Person
from disorders.models import Disorder
from treatments.models import Treatment
from symptons.models import Sympton

class Patient(Person):
	symptons=models.ManyToManyField(Sympton)
	disorders=models.ManyToManyField(Disorder)
	treatments=models.ManyToManyField(Treatment)

	class Meta:
		verbose_name = pgettext("Patient model", "Patient")
		verbose_name_plural = pgettext("Patient model", "Patients")