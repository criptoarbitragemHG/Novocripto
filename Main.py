import time
import requests
import os

TELEGRAM_BOT_TOKEN = os.getenv("7876107067:AAH_GN1FwdUAwF1nuOmxzF17fyiUZpcGHao")
TELEGRAM_USERNAME = os.getenv("@hugovinicius")

def enviar_telegram(msg):
    url = f"https://api.telegram.org/bot{7876107067:AAH_GN1FwdUAwF1nuOmxzF17fyiUZpcGHao"}/sendMessage"
    payload = {
        "chat_id": @hugovinicius,
        "text": msg
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Erro ao enviar mensagem:", e)

def verificar_arbitragem():
    # Simulação de arbitragem
    oportunidades = [
        {"moeda": "USDT", "binance": 1.00, "kucoin": 1.03, "rede": "ERC20", "liquidez": 1500},
        {"moeda": "BTC", "mexc": 60000, "foxbit": 59000, "rede": "ERC20", "liquidez": 500},
    ]
    for o in oportunidades:
        if "rede" in o and o["liquidez"] >= 1000:
            v1, v2 = list(o.values())[1], list(o.values())[2]
            dif = abs(v1 - v2) / v2 * 100
            if dif >= 2:
                msg = f"Oportunidade de arbitragem:\\n{str(o)}\\nDiferença: {dif:.2f}%"
                enviar_telegram(msg)

if __name__ == "__main__":
    while True:
        verificar_arbitragem()
        time.sleep(60)
