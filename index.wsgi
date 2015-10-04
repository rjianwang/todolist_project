#coding:utf-8
import sae

from todolist_project import wsgi

application = sae.create_wsgi_app(wsgi.application)
