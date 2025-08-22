import requests
from django.conf import settings


class SMSService:
    def __init__(self):
        self.api_id = settings.SMS_RU_API_ID
        self.base_url = "https://sms.ru/sms/send"

    def send_sms(self, phone, message):
        params = {
            'api_id': self.api_id,
            'to': phone,
            'msg': message,
            'json': 1
        }

        try:
            response = requests.get(self.base_url, params=params)
            result = response.json()

            if result['status'] == 'OK':
                return True
            return False
        except Exception as e:
            print(f"SMS sending error: {e}")
            return False