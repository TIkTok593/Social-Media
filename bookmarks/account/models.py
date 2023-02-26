from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)  # if the user has been deleted the related tuple will be deleted
    date_of_birth = models.DateField(blank=True, null=True)  # This field will be optional, and if it is empty, it's value will be Null
    photo = models.ImageField(upload_to='users/%Y/%m/%d',
                              blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
