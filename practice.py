from twitchio.ext import commands

class Bot (commands.Bot):
    viewer_activity = {}
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token= access_token , prefix='?', initial_channels=['codingwithstrangers'],
            nick = "Perfect_Virewer")
        
        
    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        print("this shit works")

        #this is how the routine starts
        self.send_racer.start()

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        # Print the contents of our message to console...
        print(message.content.encode("utf-8"))
        print(message.author.name)
    
bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.     

    

