"""
ASGI config for example project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from strawberry.channels import GraphQLProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

django_asgi_application = get_asgi_application()

from example.schema import schema  # noqa: E402

application = GraphQLProtocolTypeRouter(schema, django_application=django_asgi_application)  # type: ignore[arg-type]
