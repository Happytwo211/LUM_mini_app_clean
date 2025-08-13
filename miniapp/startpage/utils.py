import requests

def send_sms(phone, message):
    # Пример для sms.ru
    url = "https://sms.ru/sms/send"
    params = {
        "api_id": "0D3EBB66-5261-6EBF-7C01-329DF9111B47",
        "to": phone,
        "msg": message,
        "json": 1
    }
    response = requests.get(url, params=params)
    return response.json()