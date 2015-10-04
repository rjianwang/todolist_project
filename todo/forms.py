#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings

class TodoForm(forms.Form):
	content = forms.CharField(
				widget = forms.TextInput(attrs = {'class': 'form-control', 'id': 'content', 'name': 'content', 'type': 'text', 'autofocus': 'true', 'required': 'required', 'placeholder': 'What needs to be done?'}), 
				max_length = 100, 
				error_messages = {'required': 'This field is required.', }
			)

class SigninForm(forms.Form):
	email = forms.EmailField(
				widget = forms.TextInput(attrs = {"type": "text", "name": "email", "placeholder": "E-mail", "required": "required", }), 
				max_length = 20, 
				error_messages = {"required": "This field is required.", }
			)
	password = forms.CharField(
				widget = forms.PasswordInput(attrs = {"type": "password", "name": "password", "placeholder": "Password", "required": "required"}), 
				max_length = 20, 
				error_messages = {"required": "This field is required.", }
			)

class SignupForm(forms.Form):
	username = forms.CharField(
				widget = forms.TextInput(attrs = {"type": "text", "name": "username", "placeholder": "Username", "required": "required", }), 
				max_length = 20, 
				error_messages = {"required": "This field is required.", }
			)
	email = forms.EmailField(
				widget = forms.TextInput(attrs = {"type": "text", "name": "email", "placeholder": "Email", "required": "required", }), 
				max_length = 50, 
				error_messages = {"required": "This field is required.", }
			)
	password = forms.CharField(
				widget = forms.PasswordInput(attrs = {"type": "password", "name": "password", "placeholder": "Password", "required": "required", }), 
				max_length = 20, 
				error_messages = {"required": "This field is required.", }
			)
