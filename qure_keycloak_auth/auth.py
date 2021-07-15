from authlib.integrations.django_client import OAuth
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

CONF_URL = "https://accounts.qure.ai/auth/realms/users/.well-known/openid-configuration"
oauth = OAuth()
oauth.register(
    name="qure",
    server_metadata_url=CONF_URL,
    client_kwargs={"scope": "openid email profile"},
)


class AuthLibBackend(BaseBackend):
    def __init__(self) -> None:
        super().__init__()

    def authenticate(self, request):
        token = oauth.qure.authorize_access_token(request)
        userinfo = oauth.qure.parse_id_token(request, token)
        username = userinfo["preferred_username"]
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = User(username=username)
            user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
