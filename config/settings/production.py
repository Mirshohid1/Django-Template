from .base import *

import os
from datetime import timedelta


DEBUG = False
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

if os.getenv("USE_WHITENOISE", "True") == "False":
    MIDDLEWARE.remove("whitenoise.middleware.WhiteNoiseMiddleware")
    del STATICFILES_STORAGE