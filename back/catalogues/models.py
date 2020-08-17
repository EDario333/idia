# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator

# from cities_light.abstract_models import AbstractCity, AbstractRegion, AbstractCountry
# from cities_light.receivers import connect_default_signals

from cities.models import City

from django.utils.translation import pgettext
from django.utils.translation import gettext as _

# from cities.models import BaseCountry,BaseCity#,BaseRegion

from datetime import datetime,date

from cfg import app

# class Country(AbstractCountry):					# For cities-light
# class Country(BaseCountry,models.Model):
#   class Meta:
#     verbose_name = pgettext('country model', 'Country')
#     verbose_name_plural = pgettext('country model', 'Countries')

# connect_default_signals(Country)			# For cities-light

# class Region(AbstractRegion):					# For cities-light
# class Region(BaseRegion,models.Model):
#   pass

# connect_default_signals(Region)

# class City(AbstractCity):							# For cities-light
# class City(BaseCity):
  # timezone = models.CharField(max_length=40)
	# pass

# connect_default_signals(City)					# For cities-light

class MyModel(models.Model):
	def __init__(self, *args, **kwargs):
		super(MyModel, self).__init__(*args, **kwargs)

	#created_by_user = models.ForeignKey('users.Users', editable = False, on_delete=models.PROTECT, default=1, blank=False, null=False, db_column='created_by_user', verbose_name=_('Created by'), related_name='%(class)s_created_by')
	created_by_user=models.ForeignKey(\
		'users.Users', on_delete=models.PROTECT, default=1, \
		blank=False, null=False, db_column='created_by_user', \
		verbose_name=_('Created by'), related_name='%(class)s_created_by')

	created_at=models.TimeField(\
		editable=False,default=datetime.now(),\
		blank=False, null=False)

	created_when=models.DateField(\
		editable=False,default=datetime.now(),\
		blank=False, null=False)

	disabled=models.BooleanField(\
		editable=False,default=False)

	disabled_at=models.TimeField(\
		editable = False, default=None,\
		blank=True, null=True)

	disabled_when=models.DateField(\
		editable = False, default=None,\
		blank=True, null=True)

	disabled_reason=models.CharField(\
		editable=False,max_length=1024,\
		default=None, blank=True,null=True,\
		verbose_name=_('Specify the reason to disable this product'))

	dropped=models.BooleanField(editable=False,default=False)
	dropped_at=models.TimeField(editable = False, default=None, blank=True, null=True)
	dropped_when=models.DateField(editable = False, default=None, blank=True, null=True)

	dropped_reason=models.CharField(\
		editable=False,max_length=1024,\
		default=None, blank=True,null=True,\
		verbose_name=_('Specify the reason to drop this object'))

	def undrop(self):
		self.dropped = False
		self.dropped_at = None
		self.dropped_when = None
		self.dropped_reason = None
		self.save()

	def drop(self, reason=None):
		full_time = datetime.now()
		self.dropped = True
		self.dropped_at = full_time
		self.dropped_when = full_time
		self.dropped_reason = reason
		self.save()

	@property
	def created_when_fmt_mx(self):
		year = self.created_when.year
		month = str(self.created_when.month)
		day = str(self.created_when.day)
		if len(day)<2:
			day='0'+day
		if len(month)<2:
			month='0'+month
		result = str(day) + '/' + str(month) + '/' + str(year)
		return result

	class Meta:
		#proxy = True
		abstract = True

class MyModelWithDescriptionNotesComments(MyModel):
	description_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, \
		null=True, verbose_name=_("Description"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	notes_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Notes"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	comments_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Comments"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	description_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, \
		null=True, verbose_name=_("Description"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	notes_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Notes"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	comments_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Comments"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	class Meta:
		abstract = True

class MyModelWithDescription(MyModel):
	description_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, \
		null=True, verbose_name=_("Description"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	description_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, \
		null=True, verbose_name=_("Description"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	class Meta:
		abstract = True

class MyModelWithNotes(MyModel):
	#notes = models.CharField(max_length=1024, default=None, blank=True, null=True, verbose_name=_("Notes"))
	notes_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Notes"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])
		
	notes_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Notes"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	class Meta:
		abstract = True
	
class MyModelWithComments(MyModel):
	comments_es=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Comments"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	comments_en=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS, \
		default=None, blank=True, null=True, \
		verbose_name=_("Comments"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	class Meta:
		abstract = True

class ObjectWithAddress(MyModelWithDescriptionNotesComments):
	def __init__(self, *args, **kwargs):
		super(ObjectWithAddress, self).__init__(*args, **kwargs)

	city=models.ForeignKey(\
		City, on_delete=models.PROTECT, default=None, blank=False, \
		null=False, db_column="city_id", verbose_name=_("City"))

	address_line1=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS,\
		default=None,blank=False,null=False,\
		verbose_name=_("Address line 1"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	address_line2=models.TextField(\
		max_length=app.MAX_LENGTH_TEXT_FIELDS,\
		default=None,blank=True, null=True,\
		verbose_name=_("Address line 2"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_TEXT_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_TEXT_FIELDS)])

	class Meta:
		abstract = True

class ObjectWithEmail(MyModelWithDescriptionNotesComments):
	def __init__(self, *args, **kwargs):
		super(ObjectWithEmail, self).__init__(*args, **kwargs)

	email=models.EmailField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=_("Email"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	class Meta:
		abstract = True

class ObjectWithPhone(MyModelWithDescriptionNotesComments):
	def __init__(self, *args, **kwargs):
		super(ObjectWithPhone, self).__init__(*args, **kwargs)

	phone=models.CharField(\
		max_length=app.MAX_LENGTH_PHONE_FIELDS,\
		default=None,blank=False,null=False,\
		verbose_name=_("Cell phone"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_PHONE_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_PHONE_FIELDS)])

	class Meta:
		abstract = True

class PersonAddress(ObjectWithAddress):
	def __init__(self, *args, **kwargs):
		super(PersonAddress, self).__init__(*args, **kwargs)

class PersonEmail(ObjectWithEmail):
	def __init__(self, *args, **kwargs):
		super(ObjectWithEmail, self).__init__(*args, **kwargs)

class PersonPhone(ObjectWithPhone):
	def __init__(self, *args, **kwargs):
		super(ObjectWithPhone, self).__init__(*args, **kwargs)

class SocialNetwork(MyModelWithDescriptionNotesComments):
	name=models.CharField(\
		max_length=1, choices=app.SOCIAL_NETWORKS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Social network model", "Name"))

	value=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Social network model", "URL"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

class Person(MyModel):
	last_name = models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Person model", "Last name"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	mothers_last_name=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS,\
		default=None, blank=True, null=True,\
		verbose_name=pgettext("Person model", "Mothers last name"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	first_name=models.CharField(\
		max_length=app.MAX_LENGTH_VARCHAR_FIELDS, \
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Person model", "First name"),\
		validators=[MinLengthValidator(app.MIN_LENGTH_VARCHAR_FIELDS),\
		MaxLengthValidator(app.MAX_LENGTH_VARCHAR_FIELDS)])

	middle_name=models.CharField(\
		max_length=254,\
		default=None, blank=True, null=True,\
		verbose_name=pgettext("Person model", "Middle name"))

	gender=models.CharField(\
		max_length=1, choices=app.GENDERS,\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Person model", "Gender"))

	dob=models.DateField(\
		default=None, blank=False, null=False,\
		verbose_name=pgettext("Person model", "Date of birth"))

	addresses=models.ManyToManyField(PersonAddress)
	emails=models.ManyToManyField(PersonEmail)
	phones=models.ManyToManyField(PersonPhone)
	social_networks=models.ManyToManyField(SocialNetwork)

	@property
	def full_name(self):
		result=self.first_name
		if self.middle_name and self.middle_name is not None and len(self.middle_name.strip()) > 0:
			result+=' ' + str(self.middle_name)
		result+=' ' + str(self.last_name)
		if self.mothers_last_name and self.mothers_last_name is not None and len(self.mothers_last_name.strip()) > 0:
			result+=' ' + str(self.mothers_last_name)
		return result

	@property
	def gender_full_str(self):
		if self.gender=='M':
			return _("Male")
		return _('Female')
	
	@property
	def email_readable(self):
		if self.email is not None:
			return self.email
		return ''

	@property
	def cell_phone_readable(self):
		if self.cell_phone is not None:
			return self.cell_phone
		return ''

	@property
	def age(self):
		dummy=pgettext("person model", "Age")
		'''
		Code taken from https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/
		Approach 3: Efficient datetime approach,
		deal with a special case i.e. when birth date is February 29 
		and the current year is not a leap year.
		'''
		today = date.today() 
		try:  
			birthday = self.dob.replace(year = today.year) 
			# raised when birth date is February 29 
			# and the current year is not a leap year 
		except ValueError:  
			birthday = self.dob.replace(\
				year = today.year, \
					month = self.dob.month + 1, \
						day = 1) 

		if birthday > today: 
			return today.year - self.dob.year - 1
		else: 
			return today.year - self.dob.year
	
	def __str__(self):
		return self.full_name

	class Meta:
		abstract = True
		#unique_together = ('last_name', 'mothers_last_name', 'first_name', 'middle_name', 'gender', 'dob', 'city', 'address_line1')