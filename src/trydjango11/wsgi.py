"""
WSGI config for trydjango11 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import CLing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trydjango11.settings")

application = Cling(get_wsgi_application())
