from authlib.integrations.django_client import OAuth
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import Group, User
from .models import Role

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

    def create_user(self, user_info):
        user = User(
            username=user_info["preferred_username"],
            first_name=user_info["given_name"],
            last_name=user_info["family_name"],
            email=user_info["email"]
        )
        user.save()

        for group_name in user_info['groups']:
            group = Group.objects.get_or_create(name=group_name)[0]
            user.groups.add(group)

        for role_name in user_info['roles']:
            role = Role.objects.get_or_create(name=role_name)[0]
            user.roles.add(role)

        return user

    def authenticate(self, request):
        token = oauth.qure.authorize_access_token(request)
        user_info = oauth.qure.parse_id_token(request, token)

        try:
            username = user_info["preferred_username"]
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = self.create_user(user_info)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
