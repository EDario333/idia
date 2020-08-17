from rest_framework import serializers 
from .models import Disorder

class DisorderSerializer(serializers.ModelSerializer): 
	class Meta:
		model=Disorder
		# fields="__all__"
		fields = \
			('id',
			'description_es',
			'description_en',
			'notes_es',
			'notes_en',
			'comments_es',
			'comments_en',
			'code',
			'symptons',
			'dropped')