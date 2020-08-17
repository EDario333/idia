# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.utils.translation import pgettext

from symptons.models import Sympton
from axis.models import Axis
# from gravityspecifiers.models import GravitySpecifier

from catalogues.models import \
MyModelWithDescriptionNotesComments

class Disorder(MyModelWithDescriptionNotesComments):
	code=models.CharField(\
		max_length=20, default=None, blank=True, null=True,\
		verbose_name=pgettext("Disorder model","Code"), unique=True,\
		validators=[MinLengthValidator(2),MaxLengthValidator(20)])

	parent=models.OneToOneField(\
		'disorders.Disorder',on_delete=models.CASCADE,\
		default=None,blank=True,null=True,\
		verbose_name=pgettext("Disorder model","Parent"))

	symptons=models.ManyToManyField(\
		Sympton,\
		default=None,blank=False,null=False,\
		verbose_name=pgettext("Disorder model","Symptons"))

	axis=models.OneToOneField(\
		Axis,on_delete=models.PROTECT,\
		default=None,blank=False,null=False,\
		verbose_name=pgettext("Disorder model","Axis"))
	'''
	gravity=models.OneToOneField(\
		GravitySpecifier,on_delete=models.PROTECT,\
		default=None,blank=False,null=False,\
		verbose_name=pgettext("Disorder model","Gravity"))
	'''

	class Meta:
		verbose_name = pgettext("Disorder model", "Disorder")
		verbose_name_plural = pgettext("Disorder model", "Disorders")