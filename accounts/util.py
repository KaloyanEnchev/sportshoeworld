from accounts.models import Account


def get_profile() -> Account | None:
    return Account.objects.first()