import tweepy
import time
import json
from urllib.request import urlopen

def get_api_access():
	"""
		Returns the authenticated API for tweepy.

		NOTE:
		The keys are not filled in because it is a private key.
		The consumer key and access token can be easily found for 
		your twitter handle by going to app.twitter.com
		
	"""
	consumer_key = ""
	consumer_secret = ""

	access_token = ""
	access_token_secret = ""

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)

def get_crypto_information():
	"""
		Retrieves the prices of the desired crypto through the 
		coin market cap api.
	"""
	bitcoin_api = urlopen("https://api.coinmarketcap.com/v1/ticker/bitcoin")
	bitcoin_data = json.load(bitcoin_api)

	ethereum_api = urlopen("https://api.coinmarketcap.com/v1/ticker/ethereum")
	ethereum_data = json.load(ethereum_api)

	litecoin_api = urlopen("https://api.coinmarketcap.com/v1/ticker/litecoin")
	litecoin_data = json.load(litecoin_api)

	neo_api = urlopen("https://api.coinmarketcap.com/v1/ticker/neo")
	neo_data = json.load(neo_api)

	bitcoin_price = '${0:.2f}'.format(float(bitcoin_data[0]['price_usd']))
	ethereum_price = '${0:.2f}'.format(float(ethereum_data[0]['price_usd']))
	litecoin_price = '${0:.2f}'.format(float(litecoin_data[0]['price_usd']))
	neo_price = '${0:.2f}'.format(float(neo_data[0]['price_usd']))
	return bitcoin_price, ethereum_price, litecoin_price, neo_price

api = get_api_access()
bitcoin_price, ethereum_price, litecoin_price, neo_price = get_crypto_information()

message = "My cryptos current prices:\n\nBitcoin: " + bitcoin_price +"\nEthereum: " + ethereum_price + "\nLitecoin: " + litecoin_price + "\nNEO: " + neo_price + "\n\nSee you in 4 hours!"

while True:
	#Sends a tweet out every 4 hours FOREVER.
	api.update_status(status=message)
	time.sleep(14400)