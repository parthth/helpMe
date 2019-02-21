from django.contrib.auth.backends import ModelBackend
from .models import User
from django.contrib.auth.hashers import check_password

class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        try:
            user = User.objects.get(email=username)
            if check_password(password, user.password):
                #User.object
                return user
            else:
                return None

        except Exception as e:
            print(e)
            return None


    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            if user.is_active:
                return user
            else:
                return None
        except Exception as e:
            print(e)
            return None