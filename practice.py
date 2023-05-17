from twitchio.ext import commands
from clientshit import access_token

class Bot(commands.Bot):

   def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        
        super().__init__(token= access_token , prefix='?', initial_channels=['codingwithstrangers'],
            nick = "Strangest_Racer")

   
print("this shit works")
bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.