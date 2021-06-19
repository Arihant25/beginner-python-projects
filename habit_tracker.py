import requests
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv(".env")

TOKEN = os.getenv("pixela_token")
USERNAME = os.getenv("pixela_user")
EMAIL = os.getenv("email")
GRAPH_ID = "graph1"

# Create a Pixela account
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create a graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "hours",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Kolkata"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Format date as YYYYMMDD
today = date.today()
today = today.strftime("%Y%m%d")

# Add a pixel
PIXEL_ENDPOINT = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today,
    "quantity": input("How many hours did you study today?\n")
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)

# Update the profile
PROFILE_ENDPOINT = f"https://pixe.la/@{USERNAME}"
profile_config = {
    "displayName": "Arihant",
    "gravatarIconEmail": EMAIL,
    "timezone": "Asia/Kolkata",
    "pinnedGraphID": GRAPH_ID
}
# response = requests.put(url=PROFILE_ENDPOINT, json=profile_config, headers=headers)
# print(response.text)

# Update a pixel
UPDATE_PIXEL_ENDPOINT = f"{PIXEL_ENDPOINT}/20210618"
update_config = {
    "quantity": "5",
}
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_config, headers=headers)
# print(response.text)

# Delete a pixel
# response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)
