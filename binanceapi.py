import requests
import time
import os
from binance.client import Client


API_KEY_binance = "GXfFS5lUcbCKScpKH28T1uIIvUCl2au0kdSdfXhtxlT3lOic4HDCGNbwDpS3uMq7"
API_SECRET_binance = "UVocNcy51L6G94GPMAUxnDrQTimUcLs5I2LKHP990oWILRbcc2Ow5pGX2nNslV88"

client = Client(API_KEY_binance,API_SECRET_binance)



# pools = client.get_all_pools()

# def Binance(from_coin, to_coin, amount):
#     for pool in pools:
#         if from_coin in pool["assets"] and to_coin in pool["assets"]:
#             res = client.get_swap_price(quoteAsset=from_coin,baseAsset=to_coin,quoteQty=max(10,min(5000,amount)))
#             to_amount = amount * 0.9996 * float(res["price"])
#             return to_amount
#     return 0

if __name__ == "__main__":
    # print(client.get_order_book(symbol='BNBBTC'))
    # print(Binance("DAI","USDT",10))
    print("hello")