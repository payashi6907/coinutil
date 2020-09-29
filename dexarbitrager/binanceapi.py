import requests
import time
import os
from binance.client import Client



API_KEY_binance = "your_apikey"
API_SECRET_binance = "your_secretkey"
client = Client(API_KEY_binance,API_SECRET_binance)

pools = client.get_all_pools()

def Binance(from_coin, to_coin, amount):
    for pool in pools:
        if from_coin in pool["assets"] and to_coin in pool["assets"]:
            res = client.get_swap_price(quoteAsset=from_coin,baseAsset=to_coin,quoteQty=max(10,min(5000,amount)))
            to_amount = amount * 0.9996 * float(res["price"])
            return to_amount
    return 0


if __name__ == "__main__":
    print(client.get_swap_price(quoteAsset="DAI", baseAsset="USDT", quoteQty=100))
   
