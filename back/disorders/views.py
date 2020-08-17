from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework import serializers

from symptons.models import Sympton

from .models import Disorder
from .serializers import DisorderSerializer
from rest_framework.decorators import api_view

APP_NAME="Disorder"

@api_view(['GET', 'POST', 'DELETE'])
def view_all(request):
	if request.method == 'GET':
		data = Disorder.objects.all()

		title = request.GET.get('title', None)
		if title is not None:
			data = data.filter(title__icontains=title)
		
		serializer = DisorderSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
			# 'safe=False' for objects serialization

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		'''
		For v-autocomplete in front-end don't use __decode_symptons__...
		Note that with this approach new items can't be added
		'''
		# data['symptons']=__decode_symptons__(data['symptons'])

		'''
		For v-combobox in front-end use __decode_symptons__...
		Note that with this approach new items can be added
		'''
		data['symptons']=__decode_symptons__(data['symptons'])

		serializer = DisorderSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 

		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		count = Disorder.objects.all().delete()
		return JsonResponse({'message': '{} %ss were deleted successfully!'.format(count[0], APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def view_one(request, pk):
	try: 
		data = Disorder.objects.get(pk=pk) 
	except Disorder.DoesNotExist: 
		return JsonResponse({'message': 'The %s does not exist'.format(APP_NAME)}, status=status.HTTP_404_NOT_FOUND) 

	if request.method == 'GET': 
		serializer = DisorderSerializer(data) 
		return JsonResponse(serializer.data) 

	elif request.method == 'PUT': 
		data = JSONParser().parse(request) 
		serializer = DisorderSerializer(data, data=data) 
		if serializer.is_valid(): 
			serializer.save() 
			return JsonResponse(serializer.data) 
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

	elif request.method == 'DELETE': 
		data.delete() 
		return JsonResponse({'message': '%s was deleted successfully'.format(APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

def __decode_symptons__(symptons):
	res=[]
	for x in range(len(symptons)):
		s=None
		if isinstance(symptons[x],str):
			s=Sympton(description_es=symptons[x],code=symptons[x][:9])
			s.save()
			res.append(s.id)
		elif isinstance(symptons[x],dict):
			s=Sympton.objects.get(pk=symptons[x]['id'])
			res.append(s.pk)
	return res