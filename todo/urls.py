from django.conf.urls import url
from todo.views import *

urlpatterns = [
	url(r'^$', index, name = 'index'),
	url(r'^signin/$', signin, name = 'signin'),
	url(r'^signup$/', signup, name = 'signup'),
	url(r'^signout/$', signout, name = 'signout'),
	url(r'^add$', add, name = 'add'),
	url(r'^done/$', done, name = 'done'),
	url(r'^undone/$', undone, name = 'undone'),
	url(r'^delete/$', delete, name = 'delete'),
	url(r'^404/$', not_found, name = 'not_found'),
]
