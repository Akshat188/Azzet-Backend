from django.shortcuts import render
from core.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
import json
# from rest_framework.views import APIView

# from rest_framework import status
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from django.contrib.auth.models import User



# from core.models import *
# import random
# from django.core.mail import send_mail
# #  APIs: 
# #POST: Login : takes phoneNo and password return auth token
# #POST: Signup : creates a new user with all the fields
# #POST: Join : for joining a contest creates a new entry in userLeague
# #POST: Buy/Sell : Modify holdings
# #GET: getAllholdings: Portfolio view

@api_view(['POST',])
def login(request):
    print("yes")
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        username = body['username']
        password = body['password']
        print("hello")
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None :
            appUser = AppUser.objects.get(user=user)
            if appUser is not None :
                token, created = Token.objects.get_or_create(user=user)
                data={}
                data['token']=token.key
                return Response(data)
            else :
                return Response(status=401)
        else :
            return Response(status=401)
        

@api_view(['POST',])
def signUp(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        fullname = body['fullname']
        email = body['email']
        phone = body['phone']
        gender = body['gender']
        username = body['username']
        password = body['password']
        dob = body['dob']
        [user,_] = User.objects.get_or_create(username=username,password=password)
        user.save()
        appUser= AppUser.objects.create(user=user,name=fullname,email=email,mobileNo=phone,gender=gender,dob=dob)
        appUser.save()
        return Response(status=200)

@api_view(['GET',])
def getAllLiveContests(request):
	l=[]
	for i in League.objects.all():
		l.append(i.name)
	return Response(l)

@api_view(['POST',])
def joinContest(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        leaguename = body['leaguename']
        username = body['username']
        user = User.objects.get(username=username)
        league = League.objects.get(name=leaguename)
        userL,_ = UserLeague.objects.get_or_create(user=user,league=league)
        userL.save()
        return Response(status=200)

@api_view(['POST',])
def Trade(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        symbol = body['symbol']
        units = body['units']
        leaguename = body['leaguename']
        username = body['username']
        user = User.objects.get(username=username)
        league = League.objects.get(name=leaguename)
        userL,_ = UserLeague.objects.get_or_create(user=user,league=league)
        record = Holding.objects.get(userLeague=userL,stockSymbol=symbol)
        if record is None:
            holding=Holding.objects.create(userLeague=userL,stockSymbol=symbol,units=units)
            holding.save()
        else:
            record.update(units=record.units+units)
            record.save()
        return Response(status=200)
