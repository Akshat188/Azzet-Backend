from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class AppUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	mobileNo = PhoneNumberField(null=False, blank=False, unique=True) #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models
	gender = models.CharField(max_length=1, choices=[('M',"Male"),('F',"Female")])
	dob = models.DateField()

class League(models.Model):
	name = models.CharField(max_length=255)
	startTime = models.DateField()
	endTime = models.DateField()
	entryFee = models.IntegerField()
	totalSpots = models.IntegerField()
	prizePool = models.IntegerField()

class UserLeague(models.Model):
	user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
	league = models.ForeignKey(League, on_delete=models.CASCADE)
	balance = models.IntegerField(default=100000)

class Holding(models.Model):
	userLeague = models.ForeignKey(UserLeague, on_delete=models.CASCADE)
	stockSymbol = models.CharField(max_length=5)
	units = models.IntegerField()
