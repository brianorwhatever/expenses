from .production import *

DEBUG = True

MIDDLEWARE.remove('django.middleware.csrf.CsrfViewMiddleware')