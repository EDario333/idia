from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Medicament
from .serializers import MedicamentSerializer
from rest_framework.decorators import api_view

APP_NAME="Medicament"

@api_view(['GET', 'POST', 'DELETE'])
def view_all(request):
	if request.method == 'GET':
		data = Medicament.objects.all()

		title = request.GET.get('title', None)
		if title is not None:
			data = data.filter(title__icontains=title)
		
		serializer = MedicamentSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
			# 'safe=False' for objects serialization

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = MedicamentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 

		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		count = Medicament.objects.all().delete()
		return JsonResponse({'message': '{} %ss were deleted successfully!'.format(count[0], APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def view_one(request, pk):
	try: 
		data = Medicament.objects.get(pk=pk) 
	except Medicament.DoesNotExist: 
		return JsonResponse({'message': 'The %s does not exist'.format(APP_NAME)}, status=status.HTTP_404_NOT_FOUND) 

	if request.method == 'GET': 
		serializer = MedicamentSerializer(data) 
		return JsonResponse(serializer.data) 

	elif request.method == 'PUT': 
		data = JSONParser().parse(request) 
		serializer = MedicamentSerializer(data, data=data) 
		if serializer.is_valid(): 
			serializer.save() 
			return JsonResponse(serializer.data) 
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

	elif request.method == 'DELETE': 
		data.delete() 
		return JsonResponse({'message': '%s was deleted successfully'.format(APP_NAME)}, status=status.HTTP_204_NO_CONTENT)