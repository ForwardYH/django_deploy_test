"""
WSGI config for practice project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append("/home/ubuntu/.pyenv/versions/django-server/lib/python3.5/site-packages")
sys.path.append("/home/ubuntu/workspace/practice")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "practice.settings.production")

application = get_wsgi_application()
