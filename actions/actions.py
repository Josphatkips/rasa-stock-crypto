# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset
import requests
#
#
class ActionStock(Action):

    def name(self) -> Text:
        return "action_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # dispatcher.utter_message(text="Fetching Crypto price for: "+tracker.get_slot('coin'))
        url = "https://yfapi.net/v6/finance/quote"

        querystring = {"symbols":tracker.get_slot('stock')}

        headers = {
            'x-api-key': "Bu6munjw6K8nHylacyw2f2jiAI2Nb8L94VdiT9nB"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        rs=response.json()
        price=rs['quoteResponse']['result'][0]['regularMarketPrice']

        print(rs['quoteResponse']['result'][0]['regularMarketPrice'])
        dispatcher.utter_message(text="The price of: "+str(tracker.get_slot('stock').upper())+' is: '+str(price))

        return [AllSlotsReset()]

class ActionCrypto(Action):

    def name(self) -> Text:
        return "action_crypto_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        
        symbol=tracker.get_slot('coin')+'USDT'
        symbol=symbol.upper()
        querystring = {"symbol":symbol}
        response = requests.request("GET", 'https://api.binance.com/api/v3/ticker/price', params=querystring)

        rs=response.json()
        # print(tracker.get_slot('coin'))
        # print(rs)
        # print(symbol)

        # print(rs['price'])
        price=str(rs['price'])
        dispatcher.utter_message(text="Price of : "+str(tracker.get_slot('coin')) +' is: '+price)

        return [AllSlotsReset()]
