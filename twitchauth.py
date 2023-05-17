import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
client_id = os.getenv("TWITCH_CLIENT_ID")
oauth_token = os.getenv(TWITCH_OAUTH_TOKEN)

# Set up API request headers
headers = {
    "Authorization": f"Bearer {oauth_token}",
    "Client-Id": client_id
}

# Make API request to get user's channel information
response = requests.get("https://api.twitch.tv/helix/users", headers=headers)

# Check if request was successful
if response.status_code == 200:
    # Get user's channel ID from response
    data = response.json()
    user_id = data["data"][0]["id"]
    
    # Make API request to get channel information
    response = requests.get(f"https://api.twitch.tv/helix/channels?broadcaster_id={user_id}", headers=headers)
    
    # Check if request was successful
    if response.status_code == 200:
        # Get channel information from response
        data = response.json()
        channel_name = data["data"][0]["broadcaster_name"]
        game_name = data["data"][0]["game_name"]
        
        # Print channel information
        print(f"Channel Name: {channel_name}")
        print(f"Currently Playing: {game_name}")
    else:
        print(f"Error retrieving channel information. Status code: {response.status_code}")
else:
    print(f"Error retrieving user information. Status code: {response.status_code}")
