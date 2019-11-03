# Description: This is a chatbot program

#There are broadly two variants of chatbots: Rule-Based and Self learning.
#Rule-based approach, a bot answers questions based on some rules on which it is trained on
#Self learning bots are the ones that use some Machine Learning-based approach to chat

#Resource: (1) https://towardsdatascience.com/build-your-first-chatbot-using-python-nltk-5d07b027e727
#          (2) https://api.coinmarketcap.com/v1/ticker/bitcoin/
#          (3) https://api.coinmarketcap.com/v1/ticker/
#          (4) https://realpython.com/python-bitcoin-ifttt/

from nltk.chat.util import Chat, reflections
import requests
import time
from datetime import datetime

#The URL Ticker to get the .json files of the crypto currencies
TICKER_URL = 'https://api.coinmarketcap.com/v1/ticker/'

#Function to get the latest crypto currency price of a specific 'crypto' e.g bitcoin, litecoin, etc.
# crypto = {bitcoin, litecoin, etherium, ...}
def get_latest_crypto_price( crypto ):
    response = requests.get(TICKER_URL+crypto+'/')
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"(.*) (much|price) (.*)(bitcoin|btc)(.*)",
        ["The price of bitcoin when you started this chat was "+ "".join( str(get_latest_crypto_price( 'bitcoin'))),]
    ],
    [
        r"what is the price of (bitcoin-cash|bch)(.*)",
        ["The price of bitcoin-cash when you started this chat was  "+ "".join( str(get_latest_crypto_price( 'bitcoin-cash'))),]
    ],
    [
        r"(.*) (much|price) (.*) (litecoin|ltc)(.*)",
        ["The price of litecoin when you started this chat was  "+ "".join( str(get_latest_crypto_price( 'litecoin'))),]
    ],
    [
        r"(.*) (much|price) (.*)(ethereum|eth)(.*)",
        ["The price of ethereum when you started this chat was  "+ "".join( str(get_latest_crypto_price( 'ethereum'))),]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is M.W.A.P.E like in Iron Man, but you can just call me Sam and I'm your chatting companion ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing very well\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*) created ?",
        ["randerson112358 created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan',]
    ],
    [
        r"how is the weather in (.*)?",
        ["Weather in %1 is amazing like always","It's hot here in %1","It's chilli here in %1", "In %1 there is a 50% chance of rain",]
    ],
    [
        r"i work (in|at) (.*)?",
        ["%1 is an amazing company, I have heard about it.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"is it (.*) in (.*)",
        ["No its not %1 in %2","It could be", "Yes its %1 in %2"]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","LeBron", "D-Wade"]
],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["Zendaya"]
],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

#A Function to run the chatbot
def chatty():
  print("Hi, I'm M.W.A.P.E and I want to help and chat with you ! \nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
  chat = Chat(pairs,reflections )
  chat.converse()

#Run the chatbot
chatty()