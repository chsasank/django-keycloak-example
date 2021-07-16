import os
from django.conf import settings

AUTH_CONF_URL = getattr(
    settings,
    "AUTH_CONF_URL",
    "https://accounts.qure.ai/auth/realms/users/.well-known/openid-configuration",
)

AUTH_SESSION_COOKIE_AGE = getattr(settings, "AUTH_SESSION_COOKIE_AGE", 86400)  # 1 day
AUTH_SESSION_COOKIE_AGE_MOBILE = getattr(
    settings, "AUTH_SESSION_COOKIE_AGE_MOBILE", 31536000
)  # 1 year
