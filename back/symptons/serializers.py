from rest_framework import serializers 
from .models import Sympton

class SymptonSerializer(serializers.ModelSerializer): 
	class Meta:
		model=Sympton
		fields="__all__"