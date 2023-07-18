import logging; 
import csv
import os
import twitchio
import datetime
from twitchio import Message
from twitchio.ext import commands, eventsub
from configuration import CLIENT_ID, CLIENT_SECRET, TOKEN, CALLBACK, CHANNEL_NAME, BROADCASTER_ID, MODERATOR_ID, WEBHOOK_SECRET, ESCLIENT_PORT

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
_USER_CHANNEL_ID = BROADCASTER_ID
_MODERATOR_ID = MODERATOR_ID
# 9. _WEBOOK_SECRET is a >10 digit random string. If this string changes then you need to reauthorize the twitch app for every (click the 'Click this' link again).
_WEBHOOK_SECRET = WEBHOOK_SECRET
# Sometimes you have to use the delete_all_active_subscriptions() function when you restart the bot
# This is the port that the webhook will listen on locally
_ESCLIENT_PORT = ESCLIENT_PORT

# Simulate the event with twitchcli 'twitch event trigger channel.follow -s <_WEBHOOK_SECRET>  --from-user <_MODERATOR_ID> --to-user <_BROADCASTER_ID> --version 2 --forward-address <_CALLBACK>

esbot = commands.Bot.from_client_credentials(client_id=_CLIENT_ID, client_secret=_CLIENT_SECRET)
esclient = eventsub.EventSubClient(esbot, webhook_secret=_WEBHOOK_SECRET, callback_route=_CALLBACK)#, token=_TOKEN)
#dicts and global variables
racer_csv = "the_strangest_racer.csv"
strangest_racers = {}

racers_removed = {}
duplicate = set()
false_lurkers = {}
with open (racer_csv, 'w') as file:
    pass

#This will track user from 
# class Bot(commands.Bot):
    
    

    # def __init__(self):
    #     # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
    #     # prefix can be a callable, which returns a list of strings or a string...
    #     # initial_channels can also be a callable which returns a list of strings...
        
    #     super().__init__(token= _TOKEN , prefix='!', initial_channels=['codingwithstrangers'],
    #         nick = "lurkers_chats")

    
        # print(user_name)
        # # list of users to exclude
        # exclude_users = ['nightbot','streamlabs','codingwithstrangers']
        # user_name = message.author.name.lower()
        # chat = 
        # print(user_name)
    #     if user_name not in exclude_users:
    #         if user_name not in self.lurkers_chats:
    #              # Add the user's name to the lurkers_chats set
    #             self.lurkers_chats[user_name] = True
    # logger.info(lurkers_chats, 'Jimmy FTW')
                
        
            
                
        
        # #minus point from user for infractions
        # # wight one bad word they wont get any point.

        # for i in message.content.split():
        #     bad_words = ["strainbreh", "fun", "easy", "try", "why", "mod", "my wife is black", "racing game"
        #                  ,"blm" ]
        #     if i.lower() in bad_words:   
        #         if len(message.content) == 1:
        #             self.lurkers_chats[message.author.name] -= 0.5  
        #         else:
        #             self.lurkers_chats[message.author.name] -= 1.5
             
        

        # #check if user is subscriber or not
        # #if they use a channel emote "channel emote and are subbed" they are getting .5 point
        # subbed_chatters = ["coding32Thinkmybrother", "coding32Trunks", "coding32Whatmybrother", "coding32Zemi", "coding32Goten", "coding32Heart", "coding32Outofsewer"
        #                    , "coding32sewer", "coding32Suscoding", "coding32Donny", "coding32What", "coding32really", "thank you", "thanks", "thank you"]
        # for x in message.content.split():
        #     if x in subbed_chatters and message.author.is_subscriber == 1:
        #         self.points_by_chatter[message.author.name] += .5
        #         break    
        # print(self.points_by_chatter)
        # if message.author.is_subscriber:
        #     print("🌟")
        # else:
        #     print("🌘")
        


  
            
# bot = Bot()
# bot.run()


#this is the remove command 
class Bot(commands.Bot):
    @commands.command()
    async def remove(self, ctx: commands.Context):
        global strangest_racers
        print(strangest_racers)
        user= ctx.author.name.lower()
        #first check the false_lurker for true users
        if user in false_lurkers:
            await ctx.send(f'{ctx.author.name}! DADDY CHILL... you are not in the race')
            print(false_lurkers, 'Lurkers')

#this will add the user to the false lurker as true and mke the user false in the strangest racer
        else:
            if user in strangest_racers:
                strangest_racers[user] = False
                if not strangest_racers[user]:
                    false_lurkers[user] = True
                    write_to_file()
                    # message sent if they are removed
                    await ctx.send(f'Ok Ok take yo last place havin ass on then {ctx.author.name}!')
                    print(false_lurkers, 'my demon')

    async def event_message(self, message): 
        lurkers_chats = {}
        exclude_users = ['nightbot','streamlabs','codingwithstrangers']
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content.encode("utf-8"))
        print(message.author.name)
        user_name = message.author.name.lower()
        
        print(user_name, 'are you ok Annie')
        if user_name not in exclude_users:
            if user_name not in self.lurkers_chats:
                 # Add the user's name to the lurkers_chats set
                self.lurkers_chats[user_name] = True



    def __init__(self):
        super().__init__(token= TOKEN , prefix='!', initial_channels=['codingwithstrangers'],
            nick = "Perfect_Lurker")
        print("Test1")
    def __init__(self):
        super().__init__(token=_TOKEN, prefix="!", initial_channels=_CHANNEL_NAME)

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
            logger.exception(f"esclient failed to subscribe: {e}")

    async def event_ready(self):
        logger.info(f"Bot is ready!")
    print('why my shit not working?')
bot = Bot()
bot.loop.run_until_complete(bot.__ainit__())



#this will set max users and count list and add users
@esbot.event()
async def event_eventsub_notification_channel_reward_redeem(payload: eventsub.CustomReward) -> None:
    user_name = payload.data.user.name
    channel = bot.get_channel('codingwithstrangers')
    max_racers = 30
    logger.info(f"{payload.data.redeemed_at}, Redeem Event, {payload.data.id}, {payload.data.broadcaster.name}, {payload.data.user.name}, {payload.data.reward.title}, {payload.data.status}"
     )         

    #set ditc to honor max_racer and add new racers who are true in strangest racer
    if (sum (strangest_racers.values()) < max_racers) and (user_name.lower() not in strangest_racers.keys()):
        strangest_racers[user_name.lower()] = True
        logger.info(f"Added {user_name.lower()}")
        await channel.send(f'{payload.data.user.name.lower()}, Start Your Mother Loving Engines!! You are in the race Now!')
        write_to_file()
    #send a message from the bot
    else:
        logger.info(f'{user_name.lower()}, hey sorry you can only enter the race once per stream coding32Whatmybrother')
        await channel.send(f'{payload.data.user.name.lower()}, hey sorry you can only enter the race once per stream coding32Whatmybrother ') 
 


#stops the duplicate 
def write_to_file():
    print (strangest_racers, "hey look at me ")
    with open(racer_csv, 'w') as file:
        for user_name in strangest_racers.keys():
            if strangest_racers[user_name.lower()] == True:
                file.write(user_name.lower() + '\n')


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

@esbot.event()
#this is how you pull the whos folloing me
async def event_eventsub_subscribe_channel_follows_v2(payload: eventsub.ChannelFollowData) -> None:
    follows = payload.user.fetch_follow(to_user=_CHANNEL_NAME)
    #cant do it this way need token and autho of every viewer 
        
bot.run()

