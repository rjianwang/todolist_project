#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.conf import settings
from django.db.models import Q
import time, datetime
from models import *
from forms import *

# Create your views here.

def index(request):
	try:
		form = TodoForm({'content': ''})
		signin_form = SigninForm({'email': '', 'password': ''})
		signup_form = SignupForm({'username': '', 'email': '', 'password': ''})
		todos = Todo.objects.all()
	except Exception as e:
		pass

	return render(request, 'index.html', locals())

def add(request):
	try:
		form = TodoForm(request.POST)
		if form.is_valid():
			todo = Todo.objects.create(content = form.cleaned_data["content"], user_id = 1)
			todo.save()

		todos = Todo.objects.all()
	except:
		pass
#	return render(request, 'index.html', locals())
	return HttpResponseRedirect('/')

def done(request):
	try:
		form = TodoForm({'content': ""})
		id = request.GET.get('id', None)
		print id
		try:
			todo = Todo.objects.get(id = id)
			todo.status = True
			todo.save()
		except Todo.DoesNotExist:
			not_found(request)
		todos = Todo.objects.all()
	except Exception as e:
		pass
	#return render(request, 'index.html', locals())
	return HttpResponseRedirect('/')

def undone(request):
	try:
		form = TodoForm({'content': ""})
		id = request.GET.get('id', None)	
		try:
			todo = Todo.objects.get(id = id)
			todo.status = False
			todo.save()
		except Todo.DoesNotExist:
			not_found(request)
		todos = Todo.objects.all()
	except Exception as e:
		pass
	#return render(request, 'index.html', locals())
	return HttpResponseRedirect('/')

def delete(request):
	try:
		form = TodoForm({'content': ""})
		id = request.GET.get('id', None)
		print id	
		try:
			todo = Todo.objects.get(id = id)
			todo.delete()
		except Todo.DoesNotExist:
			not_found(request)
		todos = Todo.objects.all()
	except Exception as e:
		pass
	#return render(request, 'index.html', locals())
	return HttpResponseRedirect('/')

def signin(request):
	try:
		if request.method == 'POST':
			signin_form = SigninForm(request.POST)
			if signin_form.is_valid():
				username = signin_form.cleaned_data["username"]
				password = signin_form.cleaned_data["password"]
				user = authenticate(username = username, password = password)
				if user is not None:
					user.backend = "django.contrib.auth.backends.ModelBackend"
					login(request, user)
				else:
					return render(request, '404.html', {"reason": "Failed to signin"})
				return HttpResponseRedirect('/')
			else:
				return render(request, '404.html', {"reason": signin_form.errors})
	except Exception as e:
		pass
	#return render(request, 'signin.html', locals())
	return HttpResponseRedirect('/')

def signup(reqeust):
	try:
		if request.method == 'POST':
			signup_form = SignupForm(request.POST)
			if signup_form.is_valid():
				user = User.objects.create()
				user.save()

				user.backend = 'django.contrib.auth.backends.ModelBackend'
				login(request, user)
				
				return HttpResponseRedirect('/')
			else:
				return render(request, '404.html', {"reason": signup_form.errors})
		else:
			signup_form = SignupForm()
	except Exception as e:
		pass		
	#return render(request, 'signup.html', locals())
	return HttpResponseRedirect('/')

def signout(request):
	try:
		logout(request)
	except Exception as e:
		pass		
	#return redirect(request.META('HTTP_REFERER'))
	return render(request, 'signin.html', locals())

def not_found(request):
	return render(request, '404.html', locals())
