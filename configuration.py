import os
import json
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET= os.environ['CLIENT_SECRET']
TOKEN = os.environ['TOKEN']
CALLBACK = os.environ['CALLBACK']
CHANNEL_NAME = json.loads(os.environ['CHANNEL_NAME'])
USER_CHANNEL_ID = os.environ['USER_CHANNEL_ID']
MODERATOR_ID = os.environ['MODERATOR_ID']
WEBHOOK_SECRET = os.environ['WEBHOOK_SECRET']
ESCLIENT_PORT = os.environ['ESCLIENT_PORT']