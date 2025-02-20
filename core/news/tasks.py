from celery import shared_task

from common.common import send_email


@shared_task
def noti_email(email, author):
    send_email(
        body="The author {} you follow has published a new article".format(author),
        to_email=email,
        subject="Reporter: The author you follow has published a new article",
    )
