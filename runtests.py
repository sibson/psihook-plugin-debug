import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner

DIRNAME = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    DATABASE_ENGINE='sqlite3',
    DATABASE_NAME=os.path.join(DIRNAME, 'database.db'),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'psihook_debug',
    )
)

test_runner = DiscoverRunner
failures = DiscoverRunner(verbosity=1).run_tests(['psihook_debug', ])
if failures:
    sys.exit(failures)
