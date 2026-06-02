from django.urls import path

from .views import (
    signal_test,
    transaction_test
)

urlpatterns = [

    path(
        'signal-test/',
        signal_test
    ),

    path(
        'transaction-test/',
        transaction_test
    ),
]
