"""
WSGI config for BabuRentalHouse project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
settings_module = "BabuRentalHouse.settings" if "RENDER_EXTERNAL_HOSTNAME" in os.environ else "BabuRentalHouse.settings"
os.environ.setdefault('DJANGO_SETTINGS_MODULE',  settings_module)

from django.core.wsgi import get_wsgi_application



application = get_wsgi_application()
