DEBUG = False

HOST_URL = '/'

import os
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

try:
    from local_settings import *
except ImportError:
    pass
