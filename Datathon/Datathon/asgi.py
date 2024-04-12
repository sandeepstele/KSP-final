"""
ASGI config for Datathon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Datathon.settings')
django.setup()

from channels.auth import AuthMiddlewareStack 

application =ProtocolTypeRouter({
    "http": get_asgi_application(),
})
