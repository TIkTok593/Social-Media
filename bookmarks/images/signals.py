from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


@receiver(m2m_changed, sender=Image.users_like.through)  # if many-to-çmany field has changed, because a user has left or a new user is registered.
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()  # How many user is in the table of this Image
    instance.save()
