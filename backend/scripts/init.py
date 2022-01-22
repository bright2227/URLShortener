from django.conf import settings
from django_q.models import Schedule


def run():

    Schedule.objects.get_or_create(
        func='urlshortener.tasks.record_new_sh',
        schedule_type=Schedule.MINUTES,
        minutes=10,
        repeats=-1
    )

    Schedule.objects.get_or_create(
        func='urlshortener.tasks.remove_old_url',
        schedule_type=Schedule.MINUTES,
        minutes=10,
        repeats=-1
    )
    return
