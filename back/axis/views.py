from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Axis
from .serializers import AxisSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

APP_NAME="Axis"

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication, SessionAuthentication, BasicAuthentication])
def view_all(request):
	# permission_classes = (IsAuthenticated,)

	if request.method == 'GET':
		data = Axis.objects.all()

		title = request.GET.get('title', None)
		if title is not None:
			data = data.filter(title__icontains=title)
		
		serializer = AxisSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
			# 'safe=False' for objects serialization

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = AxisSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 

		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		count = Axis.objects.all().delete()
		return JsonResponse({'message': '{} %ss were deleted successfully!'.format(count[0], APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def view_one(request, pk):
	try: 
		data = Axis.objects.get(pk=pk) 
	except Axis.DoesNotExist:
		return JsonResponse({'message': 'The %s does not exist'.format(APP_NAME)}, status=status.HTTP_404_NOT_FOUND) 

	if request.method == 'GET': 
		serializer = AxisSerializer(data) 
		return JsonResponse(serializer.data) 

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		obj=Axis(pk=data["pk"])
		# serializer = AxisSerializer(data, data=data)
		serializer = AxisSerializer(obj, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE': 
		data.delete() 
		return JsonResponse({'message': '%s was deleted successfully'.format(APP_NAME)}, status=status.HTTP_204_NO_CONTENT)