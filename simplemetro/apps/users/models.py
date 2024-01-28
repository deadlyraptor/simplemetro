from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from simplemetro.apps.users.managers import UserManager

class User(AbstractUser):
    '''A custom user model easier to modify than the Django default.'''

    name = CharField(_('Name of user'), blank=True, max_length=255)
    first_name = None # type: ignore
    last_name = None # type: ignore
    email = EmailField(_('Email Address'), unique=True)
    # usernames are not needed on this site so the field is set to None
    username = None

    # use the model's email field as the unique identifier
    USERNAME_FIELD = 'email'
    # set to an empty list so that USERNAME_FIELD is not included by default
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        '''Get URL for user's detail view.
        
        Returns:
            str: URL for user detail.
        '''
        return reverse('users:detail', kwargs={'pk': self.id})