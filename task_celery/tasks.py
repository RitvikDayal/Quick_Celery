from celery.decorators import task
from celery.utils.log import get_task_logger

from celery import shared_task

from .email import send_contact_email

logger = get_task_logger(__name__)

# Task to send Contact Message
@task(name="send_contact_message_task")
def send_contact_message_task():
    logger.info("Sent Contact Email")
    print("Hello from the other side")