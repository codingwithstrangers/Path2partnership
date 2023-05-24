from twitchAPI.pubsub import PubSub
from twitchAPI.twitch import Twitch
from twitchAPI.helper import first
import asyncio
import os
import twitchio
from twitchio.ext import commands, eventsub
from dotenv import load_dotenv
load_dotenv()
 
client_id = os.environ['CLIENT_ID']
access_token = os.environ['ACCESS_TOKEN']
client_secret = os.environ['CLIENT_SECRET']
users_oauth_token = os.environ['USER_OAUTH_TOKEN']
users_channel_id = int(os.environ['USER_CHANNEL_ID'])
initial_channel = os.environ['INITIAL_CHANNEL']
web_hook =''
#  =os.environ['WEBHOOK']
call_back = 'https://1443-72-133-128-106.ngrok-free.app'
 
client = twitchio.Client(token=client_id)
client.pubsub = pubsub.PubSubPool(client)
users_using_reward = set()
REWARD_NAME = 'The Perfect Lurker'
user_channel_id = 195345186



async def run_example():
   
    twitch = await Twitch(client_id, client_secret)
    # starting up PubSub
    pubsub = PubSub(twitch)
    pubsub.start()
    # you can either start listening before or after you started pubsub.
    uuid = await pubsub.listen_whispers(user_channel_id, call_back)
    input('press ENTER to close...')
    # you do not need to unlisten to topics before stopping but you can listen and unlisten at any moment you want
    await pubsub.unlisten(uuid)
    pubsub.stop()
    await twitch.close()

asyncio.run(run_example())