from django.shortcuts import render
from core.models import *

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view
# from django.contrib.auth import authenticate, login
# from core.models import *
# import random
# from django.core.mail import send_mail
# #  APIs: 
# #POST: Login : takes phoneNo and password return auth token
# #POST: Signup : creates a new user with all the fields
# #POST: Join : for joining a contest creates a new entry in userLeague
# #POST: Buy/Sell : Modify holdings
# #GET: getAllholdings: Portfolio view

# @api_view(['POST',])
# def login_app(request):
#     print("yus")
#     # if request.method == 'POST':
#         # body_unicode = request.body.decode('utf-8')
#         # body = json.loads(body_unicode)
#         # username = body['username']
#         # password = body['password']
#         # print(username,password)
#         # user = authenticate(username=username,password=password)
#         # data = {}
#         # print("gg")
#         # print(user)
#         # if user is not None :
#         #     studen = Student.objects.get(user=user)
#         #     if studen is not None :
#         #         token, created = Token.objects.get_or_create(user=user)
#         #     #account = serializer.save()
#         #         data['token']=token.key
#         #         return Response(data)
#         #     else :
#         #         return Response(status=401)
#         # else:
#     return Response(status=401)
        