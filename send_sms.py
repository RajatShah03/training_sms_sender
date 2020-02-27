import requests

def send_sms(message, phNo, sender_id, apiKey):
    url = "https://www.fast2sms.com/dev/bulk"
    payload = f"sender_id={sender_id}&message=test&language=english&route=p&numbers={phNo}"
    headers = {
        'authorization': apiKey,
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text