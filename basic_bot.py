from twitchio.ext import commands
from dotenv import load_dotenv
import twitchio
import channel_points
import asyncio
from twitchio.ext import pubsub
# from basic_bot import Bot
import os
from dotenv import load_dotenv
# from pywitch import PyWitchRedemptions, run_forever
# from basic_bot import Bot
# from websocket import create_connection
# import time
# import json
# import random
# import threading
# from .pywitch_functions import (
#     validate_token,
#     validate_callback,
#     get_user_info,
#     pywitch_log,
#     json_eval,
# )
load_dotenv()
 
client_id = os.environ['CLIENT_ID']
access_token = os.environ['ACCESS_TOKEN']
users_oauth_token = os.environ['USER_OAUTH_TOKEN']
users_channel_id = int(os.environ['USER_CHANNEL_ID'])
initial_channel = os.environ['INITIAL_CHANNEL']
 
client = twitchio.Client(token=client_id)
client.pubsub = pubsub.PubSubPool(client)
users_using_reward = set()
REWARD_NAME = 'The Perfect Lurker'
user_channel_id = 195345186
 
class Bot(commands.Bot):
 
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=access_token, prefix='?', initial_channels=['codingwithstrangers'])
 
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print('this shit blows')

    
 
    # async def event_message(self, message):
    #     # Messages with echo set to True are messages sent by the bot...
    #     # For now we just want to ignore them...
    #     if message.echo:
    #         return
 
    #     # Print the contents of our message to console...
    #     print(message.content)
 
    #     # Since we have commands and are overriding the default `event_message`
    #     # We must let the bot know we want to handle and invoke our commands...
    #     await self.handle_commands(message)
 
    # @commands.command()
    # async def hello(self, ctx: commands.Context):
    #     # Here we have a command hello, we can invoke our command with our prefix and command name
    #     # e.g ?hello
    #     # We can also give our commands aliases (different names) to invoke with.
 
    #     # Send a hello back!
    #     # Sending a reply back to the channel is easy... Below is an example.
    #     print(f'{ctx.author.name} used ?hello')
    #     if ctx.author.name == 'codingwithstrangers':
    #         await ctx.send(f'Hello Echo!')
    #     else:
    #         await ctx.send(f'Hello {ctx.author.name}!')
    # @commands.command()
    # async def perfect_lurker_checkin(self, ctx: commands.Context):
    #     # Here we have a command hello, we can invoke our command with our prefix and command name
    #     # e.g ?hello
    #     # We can also give our commands aliases (different names) to invoke with.
 
    #     # Send a hello back!
    #     # Sending a reply back to the channel is easy... Below is an example.
    #     print(f'{ctx.author.name} checked in')
 
bot = Bot()
bot.run()
