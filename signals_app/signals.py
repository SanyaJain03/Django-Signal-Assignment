import time
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Employee, Log


@receiver(post_save, sender=Employee)
def employee_signal(sender, instance, **kwargs):

    print("\n===== SIGNAL STARTED =====")

    print(
        "Signal Thread ID:",
        threading.get_ident()
    )

    time.sleep(5)

    Log.objects.create(
        message="Employee Created"
    )

    print("===== SIGNAL FINISHED =====")
