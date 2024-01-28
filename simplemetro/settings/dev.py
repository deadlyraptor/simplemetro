from simplemetro.settings.base import * #noqa

# General
DEBUG = True
ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
INSTALLED_APPS = ['whitenoise.runserver_nostatic'] + INSTALLED_APPS #noqa

# django-debug-toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware'] #noqa

INTERNAL_IPS = ['127.0.0.1']


try:
    from .local import * #noqa
except ImportError:
    pass
