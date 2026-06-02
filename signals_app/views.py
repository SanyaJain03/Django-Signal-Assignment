import threading

from django.http import HttpResponse
from django.db import transaction

from .models import Employee


def signal_test(request):

    print(
        "View Thread ID:",
        threading.get_ident()
    )

    print("Before Save")

    Employee.objects.create(
        name="Sanya Jain"
    )

    print("After Save")

    return HttpResponse(
        "Signal Test Completed"
    )


def transaction_test(request):

    try:

        with transaction.atomic():

            Employee.objects.create(
                name="Rollback User"
            )

            raise Exception(
                "Rollback Transaction"
            )

    except Exception:

        print(
            "Transaction Rolled Back"
        )

    return HttpResponse(
        "Rollback Completed"
    )
