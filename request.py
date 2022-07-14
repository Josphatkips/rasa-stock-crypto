

import requests
import json
# url = "https://yfapi.net/v6/finance/quote"

# querystring = {"symbols":"MSFT"}

# headers = {
#     'x-api-key': "Bu6munjw6K8nHylacyw2f2jiAI2Nb8L94VdiT9nB"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# rs=response.json()

# print(rs['quoteResponse']['result'][0]['regularMarketPrice'])


# print(response.json())


# json_object = json.loads(response.json())

# json_formatted_str = json.dumps(response.json(), indent=2)

# print(json_formatted_str['quoteResponse'])




querystring = {"symbol":"ETHUSDT"}
response = requests.request("GET", 'https://api.binance.com/api/v3/ticker/price', params=querystring)

rs=response.json()

print(rs['price'])