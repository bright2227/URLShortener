from datetime import timedelta
from django.conf import settings
from django.utils import timezone
from urlshortener.models import PurgeRecord, Shortener


URL_STORE_DURATION = settings.URL_STORE_DURATION


def record_new_sh():
    sh = Shortener.objects.last()
    if sh is None:
        return

    PurgeRecord.objects.create(marked=sh)
    return


def remove_old_url():
    expire_datetime = timezone.now() - timedelta(seconds=URL_STORE_DURATION)
    p = PurgeRecord.objects.filter(created__lte=expire_datetime).last()
    if p is None:
        return

    Shortener.objects.filter(id__lte=p.id).delete()
    return
