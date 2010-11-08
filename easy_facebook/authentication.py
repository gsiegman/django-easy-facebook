from django.conf import settings
from django.contrib.auth.models import User
from easy_facebook.models import FacebookProfile

class FacebookBackend(object):
    def authenticate(self, uid=None):
        try:
            return FacebookProfile.objects.get(uid=uid).user
        except:
            return None
            
    def get_user(self, user_id=None):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
    
            