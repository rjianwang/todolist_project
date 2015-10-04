#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoManager(models.Manager):
	def distinct_date(self):
		distinct_date_list = []
		date_list = self.values('time')
		for date in date_list:
			date = date['time'].strftime('%H:%M, %b %d %Y')
			if date not in distinct_date_list:
				distinct_date_list.append(date)
		
		return distinct_date_list
	

class Todo(models.Model):
	content = models.CharField(null = False, max_length = 100)
	time = models.DateTimeField(auto_now_add = True, db_index = True)
	status = models.BooleanField(default = False)
	user = models.ForeignKey(User)
	
	objects = TodoManager()
	
	class Meta:
		verbose_name = 'Todos'
		ordering = ['-time']

	def __unicode__(self):
		return self.content
