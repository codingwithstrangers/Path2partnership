import pprint
from typing import Optional
from twitchio.ext import pubsub, commands
from configuration import *
import logging


#Debug
logging.basicConfig(level=logging.INFO) # Set this to DEBUG for more logging, INFO for regular logging
logger = logging.getLogger("twitchio.http")

#Global Variable
racer_csv = "the_strangest_racer.csv"
lurkers_points = 'lurker_points.csv' 

#custom_id for channel points
perfect_lurker_channel_id="a374b031-d275-4660-9755-9a9977e7f3ae"

#class global variables for Lurker
status_in_race = "in_race"
status_out_race = "out_race"
item_none = "none"
item_shield = "shield"
item_trap = "trap"

class Lurker:
    def __init__(self, user_name: str, image_url: str):
        self.image_url = image_url
        self.user_name = user_name
        self.race_status = status_out_race
        self.item = item_none
        self.points = 0

    def join_race(self)-> bool:
        if self.race_status == status_out_race:
            self.race_status = status_in_race
            return True
        return False

    def leave_race(self):
        self.race_status = status_out_race

    def add_points(self, delta: int):
        self.points += delta

    def equip_item(self, new_item: str):
        self.item = new_item
    
    def drop_item(self):
        self.item = item_none

        
class LurkerGang:
    def __init__(self):
        self._lurker = {}
        
    def add(self, lurker: Lurker ):
        self._lurker[lurker.user_name] = lurker

    def __getitem__(self, key:str)-> Optional[Lurker]:
        return self._lurker.get(key)
        
#write how you want the Lurkergang to work
# lurker_gang = LurkerGang()
# # lurker_racer = Lurker(user_id='Heero')
# lurker_gang.add('')

#find the person that  talked
# lurker_gang['Heero'].add_point(-1)
# chat_lurker = lurker_gang[event.sender]
# if chat_lurker is None:
#     chat_lurker = Lurker(user_id= event.sender)
#     lurker_gang.add(chat_lurker)
# if chat_lurker.race_status == status_in_race:
#     chat_lurker.add_points(-1)


#key items and status


class Bot_one(commands.Bot):
    def __init__(self):
        super().__init__(token= USER_TOKEN , prefix='!', initial_channels=['codingwithstrangers'],
            nick = "Perfect_Lurker",)
        # self.add_event(self.event_pubsub_channel_points)
        self.pubsub = pubsub.PubSubPool(self)
        self.lurker_gang = LurkerGang()
    
    async def create_or_get_lurker(self, name: str)-> Lurker:
        lower_case_name =name.lower()
        new_lurker = self.lurker_gang[lower_case_name]
        if new_lurker is None:
            user_profiles = await self.fetch_users(names=[lower_case_name])
            logger.info(user_profiles[0].profile_image)
            new_lurker =  Lurker(user_name=lower_case_name,image_url= user_profiles[0].profile_image)
            self.lurker_gang.add(new_lurker)       
            
        return new_lurker
        

    async def lurker_joins_race(self, event: pubsub.PubSubChannelPointsMessage):
        chat_lurker = await self.create_or_get_lurker(event.user.name)
        channel = self.connected_channels[0]
        
        if chat_lurker.join_race():
            await channel.send(f'@{chat_lurker.user_name}, Start Your Mother Loving Engines!! You are in the race Now!')
        else:
            await channel.send(f'@{chat_lurker.user_name}, hey sorry you can only enter the race once per stream coding32Whatmybrother ') 
     
    async def event_pubsub_channel_points(self, event: pubsub.PubSubChannelPointsMessage):
        #how to find the channel reqard point
        pprint.pprint(event.reward) #rerun in terminal look for id
        
        if event.reward.id == perfect_lurker_channel_id:
            await self.lurker_joins_race(event)

    #We want toRemove users for m Strangest racer
    #when user use !remove
    @commands.command()
    async def remove(self, ctx: commands.Context):
        print('you slippery when wet mother lover')

        print("strangest_racers")
    #     user= ctx.author.name.lower()
    #     #first check the false_lurker for true users
    #     if user in false_lurkers:
    #         await ctx.send(f'@{ctx.author.name}! DADDY CHILL... you are not in the race')
    #         print(false_lurkers, 'Lurkers')

    # #this will add the user to the false lurker as true and mke the user false in the strangest racer
    #     else:
    #         if user in strangest_racers:
    #             strangest_racers[user]['is_available'] = False
    #             # if not strangest_racers[user]:
    #             false_lurkers[user]= True
    #             # write_to_file()
    #             # message sent if they are removed
    #             await ctx.send(f'Ok Ok take yo last place havin ass on then @{ctx.author.name}!')
    #             print(false_lurkers, 'my demon')
    



    async def run(self):
        topics = [
            pubsub.channel_points(USER_TOKEN)[int(BROADCASTER_ID)],
            # pubsub.channel_points(MOD_TOKEN)[int(MODERATOR_ID)]
        ]
        await self.pubsub.subscribe_topics(topics)
        print('this shit work? pt2')
        await self.start()
        
bot= Bot_one()
bot.loop.run_until_complete(bot.run())
# bot.loop.run_until_complete(bot.__ainit__())
#START UP CODE ENDS
# @client.event()
# async def event_pubsub_channel_points(event: pubsub.PubSubChannelPointsMessage):
#     #how to find the channel reqard point
#     pprint.pprint(event.reward) #rerun in terminal look for id
#     custom_reward_id="a374b031-d275-4660-9755-9a9977e7f3ae"
#     channel = client.get_channel('codingwithstrangers')
#     max_racers = 101
#         # Check if the event's reward ID matches the custom reward ID
#     if event.reward.id == custom_reward_id:
#         user_name = event.user.name
#         print(f"User '{user_name}' redeemed the custom reward.")
#     else:
#         print("Reward ID does not match the custom reward.")

     #set ditc to honor max_racer and add new racers who are true in strangest racer
    # avialable_racers = 0
    # for values in strangest_racers.values():
    #     if values['is_available']:
    #         avialable_racers+=1
    # print(strangest_racers, "wf did I do")

    # if (avialable_racers < max_racers) and (user_name not in strangest_racers.keys()):
    #     #this is how we added the image url and to the dict.
    #     user_profiles = await client.fetch_users(names=[user_name])
    #     logger.info(user_profiles[0].profile_image)
    #     strangest_racers[user_name] = {'is_available':True,'score':0, 'image_url':user_profiles[0].profile_image}     
    #     logger.info(f"Added {user_name}")
    #     await channel.send(f'@{user_name}, Start Your Mother Loving Engines!! You are in the race Now!')
    #     write_to_file()
    # #send a message from the bot
    # else:
    #     logger.info(f'@{user_name}, hey sorry you can only enter the race once per stream coding32Whatmybrother')
    #     await channel.send(f'{user_name}, hey sorry you can only enter the race once per stream coding32Whatmybrother ') 
 

# async def main():
#     topics = [
#         # pubsub.channel_points(users_oauth_token)[int(users_channel_id)],
#         pubsub.channel_points(my_token)[int(mod_channel_id)]
#     ]
#     await client.pubsub.subscribe_topics(topics)
#     await client.start()
# print('this shit work? pt2')


# client.loop.run_until_complete(main())
# #START UP CODE ENDS