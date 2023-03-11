import datetime
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from .models import Action


def create_action(user, verb, target=None):
    now = timezone.now()
    last_minute = now - timezone.timedelta(seconds=60)
    similar_objects = Action.objects.filter(user_id=user.id,
                                            verb=verb,
                                            created__gte=last_minute)  # greate than or equal means any actions that happened after this action
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_objects = similar_objects.filter(target_ct=target_ct,
                                                 target_id=target.id)
    if not similar_objects:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False
