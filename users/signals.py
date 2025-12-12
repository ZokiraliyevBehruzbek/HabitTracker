from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import UserAward, Award


def check_awards_for_user(user):
    try:
        award = Award.objects.get(title="First Login")
        UserAward.objects.get_or_create(user=user, award=award)
    except Award.DoesNotExist:
        pass

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def handle_user_save(sender, instance, created, **kwargs):
    if created:  
        check_awards_for_user(instance)

