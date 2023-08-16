#!C:\Users\taizu\AppData\Local\Programs\Python\Python39\python.exe
"""
WSGI config for appname project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

#print("Content-Type: text/html\r\n\r\n")
#print("<h2>hello world</h2>")

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('C:/x/pj_x')
sys.path.append('C:/x/pj_x/pj_x')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_x.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] = "pj_x.settings"

application = get_wsgi_application()
