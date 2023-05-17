import twitchio
import channel_points
import asyncio
from twitchio.ext import pubsub
from basic_bot import Bot
import os
from dotenv import load_dotenv
from pywitch import PyWitchRedemptions, run_forever
from basic_bot import Bot
from websocket import create_connection
import time
import json
import random
import threading
from .pywitch_functions import (
    validate_token,
    validate_callback,
    get_user_info,
    pywitch_log,
    json_eval,
)
load_dotenv()
 
client_id = os.environ['CLIENT_ID']
users_oauth_token = os.environ['USER_OAUTH_TOKEN']
users_channel_id = int(os.environ['USER_CHANNEL_ID'])
initial_channel = os.environ['INITIAL_CHANNEL']
 
client = twitchio.Client(token=client_id)
client.pubsub = pubsub.PubSubPool(client)
users_using_reward = set()
REWARD_NAME = 'The Perfect Lurker'
user_channel_id = 195345186

print('data')

from pywitch import PyWitchTMI, run_forever

def callback(data):
    pass
    

token = client_id
channel = 'codingwithstrangers'
users = {} # Shared user list minimzes the number of requests

tmi = PyWitchTMI(
    channel = channel,
    token = token,
    callback = callback, # Optional
    users = users,       # Optional, but strongly recomended
    verbose = True,      # Optional
)
tmi.start()
tmi.send('PyWitch send a message!')
run_forever()