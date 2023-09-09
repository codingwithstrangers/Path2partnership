import twitchio
import asyncio
import pprint
from twitchio.ext import pubsub
from datetime import datetime  
from twitchio import Message, Client
from twitchio.ext import commands, eventsub
from twitchio.user import User
from configuration import CLIENT_ID, CLIENT_SECRET, MOD_TOKEN, CALLBACK, CHANNEL_NAME, BROADCASTER_ID, MODERATOR_ID, WEBHOOK_SECRET, ESCLIENT_PORT, USER_TOKEN
import logging; 

#Debug
logging.basicConfig(level=logging.DEBUG) # Set this to DEBUG for more logging, INFO for regular logging
logger = logging.getLogger("twitchio.http")

#Global Variable
_CLIENT_ID = CLIENT_ID     # Application client_id from the twitch console dashboard 
_CLIENT_SECRET = CLIENT_SECRET # App secret
_TOKEN = MOD_TOKEN
_CALLBACK = CALLBACK
_CHANNEL_NAME = CHANNEL_NAME
_USER_CHANNEL_ID = BROADCASTER_ID
_MODERATOR_ID = MODERATOR_ID
_WEBHOOK_SECRET = WEBHOOK_SECRET
_ESCLIENT_PORT = ESCLIENT_PORT
_USER_TOKEN = USER_TOKEN


#Start up Code STARTS
my_token = _TOKEN
users_oauth_token = _USER_TOKEN
users_channel_id = _USER_CHANNEL_ID
mod_channel_id = _MODERATOR_ID
client = twitchio.Client(token=my_token)
client.pubsub = pubsub.PubSubPool(client)


@client.event()
async def event_pubsub_bits(event: pubsub.PubSubBitsMessage):
    pass # do stuff on bit redemptions

@client.event()
async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
    #how to find the channel reqard point
    pprint.pprint(event.reward) #rerun in terminal look for id
    custom_reward_id="21b9ce57-7f50-445d-a58e-93f8b79033c2"
    if event.reward.id != custom_reward_id:
        return
        
    pass # do stuff on channel point redemptions

async def main():
    topics = [
        pubsub.channel_points(users_oauth_token)[int(users_channel_id)],
        pubsub.channel_points(my_token)[int(mod_channel_id)]
    ]
    await client.pubsub.subscribe_topics(topics)
    await client.start()
print('this shit work? pt2')
client.loop.run_until_complete(main())
#START UP CODE ENDS