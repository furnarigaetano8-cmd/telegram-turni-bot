import os
import datetime
import zoneinfo
import requests

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_poll():
    if not TOKEN or not CHAT_ID:
        raise ValueError("TELEGRAM_TOKEN o TELEGRAM_CHAT_ID non configurati")

    tz = zoneinfo.ZoneInfo("Europe/Rome")
    today_str = datetime.datetime.now(tz).strftime("%d/%m")

    url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"

    payload = {
        "chat_id": CHAT_ID,
        "question": f"Turni del {today_str}",
        "options": [
            "Scalamento",
            "Registrazione Multe",
            "Multe Posta",
            "Assente",
            "Resp/ Comando"
        ],
        "is_anonymous": False,
        "allows_multiple_answers": True
    }

    response = requests.post(url, json=payload, timeout=10)
    if response.status_code == 200:
        print("Sondaggio inviato con successo!")
    else:
        print(f"Errore nell'invio: {response.text}")

if __name__ == "__main__":
    send_poll()
