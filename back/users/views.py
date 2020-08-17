from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Users
from .serializers import UsersSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
# from django.db.models import Q
from django.contrib.auth import authenticate

APP_NAME="Users"

@api_view(['GET', 'POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
def view_all(request):
	# permission_classes = (IsAuthenticated,)

	if request.method == 'GET':
		# data = Users.objects.all()
		data = Users.objects.none()

		email = request.GET.get('email', None)
		if email is not None:
			# data = data.filter(email__icontains=email)
			data = Users.objects.filter(email__icontains=email)
		
		serializer = UsersSerializer(data, many=True)
		# 'safe=False' for objects serialization
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		data["password"]=make_password(data["password"])
		serializer = UsersSerializer(data=data)
		if serializer.is_valid():
			res=serializer.save()
			# print(res)
			token = Token.objects.create(user=res)
			# print(token.key)
			return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)

		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	elif request.method == 'DELETE':
		count = Users.objects.all().delete()
		return JsonResponse({'message': '{} %ss were deleted successfully!'.format(count[0], APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def view_one(request, pk):
	try: 
		data = Users.objects.get(pk=pk) 
	except Users.DoesNotExist: 
		return JsonResponse({'message': 'The %s does not exist'.format(APP_NAME)}, status=status.HTTP_404_NOT_FOUND) 

	if request.method == 'GET': 
		serializer = UsersSerializer(data)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT': 
		data = JSONParser().parse(request)
		obj=Users(pk=data["pk"])
		# serializer = UsersSerializer(data, data=data)
		serializer = UsersSerializer(obj, data=data)
		if serializer.is_valid(): 
			serializer.save() 
			return JsonResponse(serializer.data) 
		return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

	elif request.method == 'DELETE': 
		data.delete()
		return JsonResponse({'message': '%s was deleted successfully'.format(APP_NAME)}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
	uname=request.POST.get('username',None)
	if uname is None:
		raise ValueError("Missed username at app/users/views.py@login(request)")

	upass=request.POST.get('password',None)
	if upass is None:
		raise ValueError("Missed password at app/users/views.py@login(request)")

	user = authenticate(username=uname, password=upass)
	print(user)
	if user is not None:
		serializer = UsersSerializer(user)
		print("serializer")
		print(serializer)
		print("serializer.data")
		print(serializer.data)
		return JsonResponse(serializer.data)
	else:
		res["status"]="error"
		res["msg"]="User does not exists"
		return JsonResponse(res, status=401)