import requests

def send_sms(phone, message):
    # Пример для sms.ru
    url = "https://sms.ru/sms/send"
    params = {
        "api_id": "D2409AE6-2B0E-AEAC-6933-00B72EDD341C",
        "to": phone,
        "msg": message,
        "json": 1
    }
    response = requests.get(url, params=params)
    return response.json()

