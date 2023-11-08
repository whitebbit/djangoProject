from celery import shared_task
from django.conf import settings
from twilio.rest import Client

# Access the settings directly
twilio_account_sid = settings.TWILIO_ACCOUNT_SID
twilio_auth_token = settings.TWILIO_AUTH_TOKEN

# Create a Twilio client using the obtained settings
# client = Client(twilio_account_sid, twilio_auth_token)


@shared_task
def send_sms(phone_number, body):
    return
    message = client.messages.create(
        body=body, from_=settings.TWILIO_NUMBER, to=phone_number
    )
    return message.sid
