from celery import shared_task
from .models import Recipient
from notion_client import Client
from django.core.mail import send_mail

@shared_task
def check_notion_updates_and_send_emails():
    notion = Client(auth='your_notion_integration_token')
    database_id = 'your_database_id'

    # Fetch pages from Notion (adjust query if needed)
    response = notion.databases.query(**{"database_id": database_id})

    # Extract required information from response
    # This part will depend on your Notion database structure

    # Fetch recipients from the database
    recipients = Recipient.objects.all()

    # Construct the email body (based on Notion response)
    email_body = 'Content from your Notion database'

    # Send emails to all recipients
    for recipient in recipients:
        send_mail(
            'Update from Notion',
            email_body,
            'from@example.com',
            [recipient.email],
            fail_silently=False,
        )
