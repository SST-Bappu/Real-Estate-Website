from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

class registraion(APIView):
    permissions_classes=(permissions.AllowAny,)
    
    def post(self,request,format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if len(password)<7:
                return Response('Password is too short')
            if User.objects.filter(email=email).exists():
                return Response('There is already an account with this email')
            user = User.objects.create(name=name,email=email,password=password)
            user.save()
            return Response('User created successfully')
        else:
            return Response('Passwords do not match')
