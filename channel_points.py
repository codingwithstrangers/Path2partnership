import twitchio
import os
import asyncio
from twitchio.ext import pubsub
from dotenv import load_dotenv
load_dotenv()

token = os.environ['ACCESS_TOKEN']
client = twitchio.Client(token)
client.pubsub = pubsub.PubSubPool(client)
users_using_reward = set()
REWARD_NAME = 'The Perfect Lurker'
@client.event()
# Define a function to handle Redemption events
async def handle_redemption(redemption_event):
    # Check if the redemption is for the "Perfect Racer" reward
    if redemption_event.reward.title == REWARD_NAME:
        # Retrieve the username of the user who redeemed the points
        username = redemption_event.user.name
        # Add the username to the set of users using the reward
        users_using_reward.add(username)
        # Print the updated set of usernames to the console
        print(f"Users using {REWARD_NAME}: {users_using_reward}")
    print('event')
# async def handle_pubsub_event(event: pubsub.PubSubChannelPointsMessage):
    
#     if event.message.type == 'reward-redeemed':
#         reward_id = event.message.data['redemption']['reward']['id']
#         if reward_id == 'your_reward_id' and event.message.data['redemption']['user_input'] == 'strangest-racer' and event.message.data['redemption']['user']['points_balance'] >= 10:
#             print('bazinga')
 
# async def on_connect():
#     await client.pubsub.subscribe('channel-points-rewards-redemption.' + client.nick + '.' + str(client.channel_id))
 
    client.run()