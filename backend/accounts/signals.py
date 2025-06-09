from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now

@receiver(user_logged_in)
def update_last_login_time(sender, user, request, **kwargs):
    user.last_login_time = now()
    user.save()
