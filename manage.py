#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          os.environ['DJANGO_SETTINGS'])
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django #noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

    
    execute_from_command_line(sys.argv)