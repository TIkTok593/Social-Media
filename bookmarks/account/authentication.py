from django.contrib.auth.models import User
from account.models import Profile


def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """

    Profile.objects.get_or_create(user=user)


class EmailAuthBackend:
    """
    Authenticate Using an email address, not only the username.
    So, If you enter either your username or email it'll succeed.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist or User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
