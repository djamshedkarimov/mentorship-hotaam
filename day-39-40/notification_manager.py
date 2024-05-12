from twilio.rest import Client

TWILIO_SID = "AC462a8a290c93f8a96f553ca0259cf9b3"
TWILIO_AUTH_TOKEN = "90277e0edcaf7129e4da080c331dd1ba"
TWILIO_VIRTUAL_NUMBER = "+18889076915"
TWILIO_VERIFIED_NUMBER = "9499961930"
'''twilio stuff'''


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
        '''class for notifications'''
