import logging; 
import csv
import os
import subprocess
import time
from typing import List
import twitchio
from datetime import datetime  
from twitchio import Message, Client
from twitchio.ext import commands, eventsub
from twitchio.user import User
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
client = Client(token=_TOKEN)
#dicts and global variables
racer_csv = "the_strangest_racer.csv"
strangest_racers = {}
lurkers_points = 'lurker_points.csv' 
racers_removed = {}
duplicate = set()
false_lurkers = {}
with open (racer_csv, 'w') as file:
    pass

#this is the remove command 
class Bot(commands.Bot):
    
    def __init__(self):
        self.lurkers_chats = []
        super().__init__(token= TOKEN , prefix='!', initial_channels=['codingwithstrangers'],
            nick = "Perfect_Lurker")
        
    async def event_message(self, message): 
        exclude_users = ['nightbot','streamlabs','codingwithstrangers', 'sockheadrps']
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
                self.lurkers_chats.append(user_name)
        
      
        def update_csv():
            talking_lurkers = self.lurkers_chats
            #read csv to compare to talking lurkers
            update_rows = []
            with open (lurkers_points, 'r') as file:
                reader = csv.reader(file)

                #loopsome ish through the rows
                for row in reader:
                    name = row[0] #names mus be in column A
                #loop for the score too
                    if name == user_name:
                        score = int(row[1])
                        #subtract some ish if its more than 1
                        score = max(score- 1 , 0)
                        
                        #update score
                        row[1] = str(score)

                        if name in talking_lurkers:
                            #remove name from talking lurker
                            talking_lurkers.remove(name)
                    update_rows.append(row)
                        #add updated row from above bck in
                        # update_rows(row)
                
            #write this to csv
            with open(lurkers_points, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(update_rows)
        update_csv()
# file.write(f"{user_name.lower()},{strangest_racers[user_name.lower()]['image_url']}\n")

        await self.handle_commands(message)

    @commands.command()
    async def remove(self, ctx: commands.Context):
        print('you slippery when wet mother lover')
        # global strangest_racers
        print(strangest_racers)
        user= ctx.author.name.lower()
        #first check the false_lurker for true users
        if user in false_lurkers:
            await ctx.send(f'@{ctx.author.name}! DADDY CHILL... you are not in the race')
            print(false_lurkers, 'Lurkers')

    #this will add the user to the false lurker as true and mke the user false in the strangest racer
        else:
            if user in strangest_racers:
                strangest_racers[user]['is_available'] = False
                # if not strangest_racers[user]:
                false_lurkers[user]= True
                write_to_file()
                # message sent if they are removed
                await ctx.send(f'Ok Ok take yo last place havin ass on then @{ctx.author.name}!')
                print(false_lurkers, 'my demon')

    @commands.command()
    #make command for txt file
    async def perfect_lurker(self, ctx: commands.Context):
        if ctx.author.is_broadcaster or ctx.author.is_mod:
            print('Iam the boss')
            #make a list
            # Create a list to store the data
            racer_data = {}
            # Open the CSV file
            with open('lurker_points.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row (if any)

                # Iterate through each row in the CSV and append it to racer_data
                for row in reader:
                    if len(row) >= 3:
                        username = row[0]
                        score = int(row[1])
                        url = row[2] if len(row) > 2 else ''
                        racer_data[username] = {'score': score, 'url': url}

                # Sort the racer_data dictionary by the 'score' key in descending order
                sorted_racer_data = dict(sorted(racer_data.items(), key=lambda x: x[1]['score'], reverse=True))
                # Get the top 3 usernames
                top_usernames = list(sorted_racer_data.keys())[:3]
                current_date = datetime.now().strftime('%Y-%m-%d')
                for username in top_usernames:
                    racer_data[username]['date'] = current_date

            # Write the racer_data to 'lurkers_data.csv'
        # ...

            # Open the CSV file for writing with the 'with' block
            with open('lurkers_data.csv', 'a', newline='') as csvfile:
                fieldnames = ['username', 'score', 'url', 'date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                for username, data in racer_data.items():
                    # Check if 'date' key is missing in data dictionary, and add it
                    if 'date' not in data:
                        data['date'] = current_date
                    writer.writerow({'username': username, 'score': data['score'], 'url': data['url'], 'date': data['date']})
                # Create a text file for each of the top 3 users
                for i, username in enumerate(top_usernames):
                    with open(f'{i+1}st_place.txt', 'w') as text_file:
                        text_file.write(username + '\n')
                        text_file.write(str(racer_data[username]['score']))
            # ...

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
    max_racers = 100
    logger.info(f"{payload.data.redeemed_at}, Redeem Event, {payload.data.id}, {payload.data.broadcaster.name}, {payload.data.user.name}, {payload.data.reward.title}, {payload.data.status}"
     )         

    #set ditc to honor max_racer and add new racers who are true in strangest racer
    avialable_racers = 0
    for values in strangest_racers.values():
        if values['is_available']:
            avialable_racers+=1
    print(strangest_racers, "wf did I do")

    if (avialable_racers < max_racers) and (user_name.lower() not in strangest_racers.keys()):
        #this is how we added the image url and to the dict.
        user_profiles = await client.fetch_users(names=[user_name])
        logger.info(user_profiles[0].profile_image)
        strangest_racers[user_name.lower()] = {'is_available':True,'score':0, 'image_url':user_profiles[0].profile_image}     
        logger.info(f"Added {user_name.lower()}")
        await channel.send(f'@{payload.data.user.name.lower()}, Start Your Mother Loving Engines!! You are in the race Now!')
        write_to_file()
    #send a message from the bot
    else:
        logger.info(f'@{user_name.lower()}, hey sorry you can only enter the race once per stream coding32Whatmybrother')
        await channel.send(f'{payload.data.user.name.lower()}, hey sorry you can only enter the race once per stream coding32Whatmybrother ') 
 


#stops the duplicate 
def write_to_file():
    print (strangest_racers, "hey look at me ")
    with open(racer_csv, 'w') as file:
        for user_name in strangest_racers.keys():
            if strangest_racers[user_name.lower()]['is_available'] == True:
                strangest_racers[user_name.lower()]['score'] = 0
                file.write(f"{user_name.lower()},{strangest_racers[user_name.lower()]['score']},{strangest_racers[user_name.lower()]['image_url']}\n")

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
