from rest_framework import serializers 
from .models import GravitySpecifier

class GravitySpecifierSerializer(serializers.ModelSerializer): 
	class Meta:
		model=GravitySpecifier
		fields="__all__"