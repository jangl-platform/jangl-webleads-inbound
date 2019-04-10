#!/usr/bin/env python
import os
import sys

from django.conf import settings

# SETTINGS
if not settings.configured:
    this_module = os.path.splitext(os.path.split(__file__)[1])[0]
    settings.configure(**{
        'DEBUG': True,
        'ROOT_URLCONF': this_module,
        'DATABASES': {'default': {}}
    })

urlpatterns = []

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
