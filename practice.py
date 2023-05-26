import logging; 
import os
import twitchio
import datetime
from twitchio.ext import commands, eventsub
from configuration import CLIENT_ID, CLIENT_SECRET, TOKEN, CALLBACK, CHANNEL_NAME, USER_CHANNEL_ID, MODERATOR_ID, WEBHOOK_SECRET, ESCLIENT_PORT

logging.basicConfig(level=logging.INFO) # Set this to DEBUG for more logging, INFO for regular logging
logger = logging.getLogger("twitchio.http")


#(Optional) 1. Go to https://dev.twitch.tv/console/apps/ and create an app
#(Optional) 2. Download and install https://dev.twitch.tv/docs/cli/ 
#(Optional) 3. Configure twitchcli command 'twitch configure' with client_id and _client_secret from step 1
_CLIENT_ID = CLIENT_ID     # Application client_id from the twitch console dashboard 
_CLIENT_SECRET = CLIENT_SECRET # App secret
# 4.0 Register a new twitch account to be used for the bot
# 4.1 Generate a token for the chatbot with scopes(twitchtokengenerator is fine for now): 
#   twitch token -s 'chat:read user:read:follows'
_TOKEN = TOKEN
# 5.0 Register with the github account at https://ngrok.com
# 5.1 Download and install ngrok on your local machine to create a websocket tunel
# 5.2 Start ngrok with 'ngrok http 4000'. This will act as our webhook and the url hast to be the same as in the twitch developer console
_CALLBACK = CALLBACK
_CHANNEL_NAME = CHANNEL_NAME
_USER_CHANNEL_ID = USER_CHANNEL_ID
_MODERATOR_ID = MODERATOR_ID
# 9. _WEBOOK_SECRET is a >10 digit random string. If this string changes then you need to reauthorize the twitch app for every (click the 'Click this' link again).
_WEBHOOK_SECRET = WEBHOOK_SECRET
# Sometimes you have to use the delete_all_active_subscriptions() function when you restart the bot
# This is the port that the webhook will listen on locally
_ESCLIENT_PORT = ESCLIENT_PORT

# Simulate the event with twitchcli 'twitch event trigger channel.follow -s <_WEBHOOK_SECRET>  --from-user <_MODERATOR_ID> --to-user <_BROADCASTER_ID> --version 2 --forward-address <_CALLBACK>

esbot = commands.Bot.from_client_credentials(client_id=_CLIENT_ID, client_secret=_CLIENT_SECRET)
esclient = eventsub.EventSubClient(esbot, webhook_secret=_WEBHOOK_SECRET, callback_route=_CALLBACK)#, token=_TOKEN)


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=_TOKEN, prefix="?", initial_channels=_CHANNEL_NAME)

    async def __ainit__(self) -> None:
        self.loop.create_task(esclient.listen(port=_ESCLIENT_PORT))
#        await esclient.delete_all_active_subscriptions()
#        logger.debug(f"Deleted all subscriptions")
        try:
            await esclient.subscribe_channel_follows_v2(broadcaster=_USER_CHANNEL_ID, moderator=_MODERATOR_ID)
            await esclient.subscribe_channel_shoutout_receive(broadcaster=_USER_CHANNEL_ID, moderator=_MODERATOR_ID)
            await esclient.subscribe_channel_points_redeemed(broadcaster=_USER_CHANNEL_ID)
            logger.debug(f"Subscribed esclient to subscribe_channel_follows_v2")
        except twitchio.HTTPException as e:
            logger.error(f"esclient failed to subscribe: {e}")

    async def event_ready(self):
        logger.info(f"Bot is ready!")
    print('why my shit not working?')
bot = Bot()
bot.loop.run_until_complete(bot.__ainit__())

# __slots__ = "_http", _USER_CHANNEL_ID, "id", "user_id", "user_name", "input", "status", "redeemed_at", "reward"
# # The __slots__ attribute restricts the instance attributes of the class to the listed names for memory efficiency.
# users_in_race = {}
# redeemed_at = datetime
# def __init__(self, obj: dict, http: _CALLBACK, parent: Optional[CustomReward]):
#     self._http = http
#     self._broadcaster_id = obj[_USER_CHANNEL_ID]
#     # Assign the value of the "broadcaster_id" key from the obj dictionary to _broadcaster_id.

#     self.id = obj["id"]
#     # Assign the value of the "id" key from the obj dictionary to id.

#     self.user_id = int(obj["user_id"])
#     # Assign the value of the "user_id" key from the obj dictionary to user_id after converting it to an integer.

#     self.user_name = obj["user_name"]
#     # Assign the value of the "user_name" key from the obj dictionary to user_name.

#     self.input = obj["user_input"]
#     # Assign the value of the "user_input" key from the obj dictionary to input.

#     self.status = obj["status"]
#     # Assign the value of the "status" key from the obj dictionary to status.

#     self.redeemed_at = parse_timestamp(obj["redeemed_at"])
#     # Assign the result of parse_timestamp function with the value of the "redeemed_at" key from the obj dictionary to redeemed_at.
#     # Note: The parse_timestamp function is assumed to be defined elsewhere.

#     self.reward = parent or obj["reward"]
#     # Assign the value of the parent parameter if it is not None, otherwise assign the value of the "reward" key from the obj dictionary to reward.

# def __repr__(self):
# return f"<CustomRewardRedemption id={self.id} user_id={self.user_id} user_name={self.user_name} input={self.input} status={self.status} redeemed_at={self.redeemed_at}>"
# # Returns a string representation of the class instance, displaying the values of id, user_id, user_name, input, status, and redeemed_at.
strangest_racers ={}
@esbot.event()
#this is how you pull the events for ONLY custom channel point this is only listening (may block other listeners)
async def event_eventsub_notification_channel_points_redeemed(payload: eventsub.CustomReward)-> None:
#Adding Racers to my dict.
    user_name = payload.data.user.name
    if user_name in strangest_racers:
        logger.info(f"{payload.redemptions_current_stream}, Channel Point Event, {payload.data.user.name}")
        #send message that racer is in race
        await esbot.send_message(user_name, "Hey don't text and drive! You are already in the RACE!")
    else:
        strangest_racers[user_name] = True
        logger.info(f"{payload.redemptions_current_stream}, Channel Point Event, {payload.data.user.name}")
        #send message racer has joined
        await esbot.send_message(user_name, "START your Engine!")
    
    print_names()

    def print_names():
        names = list(strangest_racers.keys())
        print("Names in strange_racers dictionary:")
        for name in names:
            print(name)


@esbot.event()
#this is how you pull the events for ONLY SHoutout to me this is only listening (may block other listeners)
async def event_eventsub_notification_channel_shoutout_receive(payload: eventsub.ChannelShoutoutReceiveData) -> None:
    logger.info(f"{payload.data.started_at}, Shoutout Event, {payload.data.user.name}")

@esbot.event()
#this is how you pull the events for ONLY SHoutout to me this is only listening (may block other listeners)
async def event_eventsub_notification_followV2(payload: eventsub.ChannelFollowData) -> None:
    logger.info(f"{payload.data.followed_at}, Follow Event, {payload.data.user.name}, {payload.data.broadcaster.name}") #this uses the payload timestamp instead
#    channel = esbot.get_channel('channel')
#    channel = esbot.get_channel(payload.data.broadcaster.name)
#    await channel.send(f"{payload.data.user.name} followed KreyGasm!")

bot.run()
