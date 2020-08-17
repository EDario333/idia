from rest_framework import serializers 
from .models import Axis

class AxisSerializer(serializers.ModelSerializer): 
	class Meta:
		model=Axis
		fields = \
			('id',
			'name_es',
			'name_en',
			'comments_es',
			'comments_en',
			'description_es',
			'description_en',
			'dropped')
		# fields="__all__"