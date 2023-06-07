from django.contrib import messages 
from django.contrib.auth  import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
import re

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def validate_email(email):
	pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
	return re.match(pattern, email) is not None

def sign_up (request):
	if request.method == "POST":
		# Get the post parameters
		name = request.POST['name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		# Validations
		# Check whether the email provided is accurate or not
		if(not validate_email(email)):
			messages.error(request, "Entered Email is incorrect, can you check again?")
			return redirect('/')

		# Check whether both the password provided are same or not
		if(password != confirm_password):
			messages.error(request, "Password didn't match :(")
			return redirect('/')
		
		# Check whether a user with same usernam exists or not
		user = User.objects.filter(username = username)
		if user.exists():
			messages.error(request, "Uh Oh! Username is already in use. Can you try something else?")
			return redirect('/')
		
		# Create the user
		user = User.objects.create_user(username, email)
		user.set_password(password)
		user.save()

		# Log in user after signup
		user = authenticate(username = username, password = password)
		auth_login(request, user)
		
		return redirect('/')
	
	return redirect('/404')

def sign_in (request):
	if request.method == "POST":
		# Get the post parameters
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user is not None:
			auth_login(request, user)

			user_profile = User.objects.get(username = username)
			return redirect("/")
		else:
			messages.error(request, "Invalid credentials! Please try again")
	
	return redirect('/404')