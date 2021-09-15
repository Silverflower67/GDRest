import gd
from starlette.authentication import (AuthenticationBackend, AuthenticationError, BaseUser, AuthCredentials)
from starlette.requests import Request
import base64
import binascii


class APIUser(BaseUser):
    def __init__(self, client: gd.Client):
        self.client = client
        self.username = client.user.name

    @property
    def is_authenticated(self) -> bool:
        return self.client.is_logged()

    @property
    def display_name(self) -> str:
        return self.username

    @property
    def identity(self) -> str:
        return self.username


class GDAuthBackend(AuthenticationBackend):
    async def authenticate(self, request: Request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != 'basic':
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError('Invalid basic auth credentials')

        username, _, password = decoded.partition(":")
        client = gd.Client()
        await client.login(username, password)
        user = await client.user.get_user()
        if user.is_mod():
            if user.is_mod(gd.Role.ELDER_MODERATOR):
                return AuthCredentials(["authenticated", "mod", "elder"]), APIUser(client)
            else:
                return AuthCredentials(["authenticated", "mod"]), APIUser(client)
        return AuthCredentials(["authenticated"]), APIUser(client)


def auth_client(user: APIUser):
    if user.is_authenticated:
        return user.client
    else:
        return gd.Client()
