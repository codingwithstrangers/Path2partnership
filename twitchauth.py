import clientshit
import requests

# Set the grant type
GRANT_TYPE = "client_credentials"

# Set the URL for the token request
TOKEN_URL = "https://id.twitch.tv/oauth2/token"

# Set the request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Client-ID": clientshit.client_id,
    "Client-SECRET": clientshit.client_id,
    "Authorization": f"Basic {clientshit.client_secret}"
}

# Set the request data
data = {
    "grant_type": GRANT_TYPE,
    "scope": "chat:read"
}

# Make the request to generate a new access token
response = requests.post(TOKEN_URL, headers=headers, data=data)

# If the request is successful
if response.status_code == 200:
    # Extract the new access token
    access_token = response.json()["access_token"]

    # Update the clientshit module with the new access token
    clientshit.access_token = access_token

    print("Access token obtained successfully!")
else:
    print("Error obtaining access token")
    print("Response status code:", response.status_code)
    print("Response text:", response.text)

# import requests
# import time
# import os

# # Set the path to the clientshit.py file
# CLIENTSHIT_PATH = "F:/Coding with Strangers/Twitchbot/perfectstrangerbot/clientshit.py"

# # Set the grant type
# GRANT_TYPE = "refresh_token"

# # Set the URL for the token request
# TOKEN_URL = "https://id.twitch.tv/oauth2/token"

# # Load the client ID, client secret, and refresh token from the clientshit.py file
# with open(CLIENTSHIT_PATH, "r") as f:
#     lines = f.readlines()
#     client_id = lines[0].strip()
#     client_secret = lines[1].strip()
#     refresh_token = lines[2].strip()

# # Set the request headers
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Client-ID": client_id,
#     "Authorization": f"Basic {client_secret}"
# }

# # Set the request data
# data = {
#     "grant_type": GRANT_TYPE,
#     "refresh_token": refresh_token
# }

# # Set the refresh interval (in seconds)
# REFRESH_INTERVAL = 3600  # refresh every hour

# def refresh_access_token():
#     """Function to refresh the access token"""
#     # Make the request to generate a new access token
#     response = requests.post(TOKEN_URL, headers=headers, data=data)
# response = requests.post(TOKEN_URL, headers=headers, data=data)

# # If the request is successful
# if response.status_code == 200:
    
#     # Extract the new access token
#     access_token = response.json()["access_token"]

#     # Update the clientshit.py file with the new access token
#     with open(CLIENTSHIT_PATH, "w") as f:
#         f.write(f"client_id = {client_id}\n")
#         f.write(f"client_secret = {client_secret}\n")
#         f.write(f"access_token = {access_token}\n")

#     print("Access token refreshed successfully!")
# else:
#     print("Error refreshing access token")

# refresh_access_token()
# import requests
# from urllib.parse import urlencode
# from clientshit import client_id , client_secret

# query_string = urlencode({'client_id': client_id, 'client_secret': client_secret, "grant_type": "client_credentials"})

# #r format is good for udeveloperxrl stringsand, a \ is a special character in a string
# twitch_url_prefix = r'https://id.twitch.tv/oauth2/token?'

# finished_endpoint = twitch_url_prefix + query_string

# #meta data that I have to send behind the scenes with your post request
# headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# #Send the post request with the correct header 
# respond = requests.post(finished_endpoint, headers=headers)

# #print content contents (do off stream)
# print(respond.content, "sockheadrps is the F####ing man")
