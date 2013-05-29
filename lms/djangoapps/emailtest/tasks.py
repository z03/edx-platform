from djcelery import celery
from django.core.mail import send_email

@celery.task
def email_task(subject, message, from_addr, to_list):
    send_email(subject, message, from_addr, to_list)
