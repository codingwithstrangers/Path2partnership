from twitchio.ext import commands
from dotenv import load_dotenv
import twitchio
import channel_points
import asyncio
from twitchio.ext import pubsub
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
web_hook =os.environ['WEBHOOK']
call_back = 'https://1443-72-133-128-106.ngrok-free.app'
 
client = twitchio.Client(token=client_id)
client.pubsub = pubsub.PubSubPool(client)
users_using_reward = set()
REWARD_NAME = 'The Perfect Lurker'
user_channel_id = 195345186

esbot = commands.Bot.from_client_credentials(client_id= client_id, client_secret=client_secret)
esclient = eventsub.EventSubClient(esbot, webhook_secret= web_hook, callback_route= call_back)
 
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


    async def __ainit__(self) -> None:
        self.loop.create_task(esclient.listen(port=4040))
        try:
            await esclient.subscribe_channel_follows_v2(broadcaster= user_channel_id, moderator=user_channel_id)
        except twitchio.HTTPException:
            pass

    async def event_ready(self):
        print("Bot is ready!")

    @esbot.event()
    async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
        print(event)
        pass # do stuff on channel point redemptions
        print("Received event!")
    async def __ainit__(self) -> None:
            self.loop.create_task(esclient.listen(port=4040))
            try:
                await esclient.subscribe_channel_follows_v2(broadcaster= user_channel_id, moderator=user_channel_id)
            except twitchio.HTTPException:
                pass  

bot = Bot()
bot.loop.run_until_complete(bot.__ainit__())




@esbot.event()
async def event_eventsub_notification_followV2(payload: eventsub.ChannelFollowData) -> None:
    print("Received event!")
    channel = bot.get_channel("codingwithstrangers")
    await channel.send(f"{payload.data.user.name} followed woohoo!")        


bot.run()
