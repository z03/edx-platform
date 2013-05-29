from djcelery import celery
from django.core.mail import send_mail

@celery.task
def email_task(subject, message, from_addr, to_list):
    send_mail(subject, message, from_addr, to_list)
