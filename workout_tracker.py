import requests
import os
from datetime import date
import time
from dotenv import load_dotenv

load_dotenv('.env')  # Get environment variables

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
# Change these to your own details
SHEETY_ENDPOINT = os.getenv("workout_endpoint")
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
GENDER = "male"
WEIGHT_KG = 65.4
HEIGHT_CM = 167.6
AGE = 16

nutritionix_headers = {
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-remote-user-id": "0"
}

nutritionix_params = {
    "query": input("Tell me which exercise you did and how much: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Understand the user's natural language query
response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_params, headers=nutritionix_headers)
data = response.json()

# Add each workout in a new row in the spreadsheet
for workout in data["exercises"]:
    sheety_params = {
        "workout": {
            "date": date.today().strftime("%d/%m/%Y"),  # Get today's date
            "time": time.strftime("%H:%M:%S", time.localtime()),  # Get the current time
            "exercise": workout["name"].title(),  # Get the name of the workout
            "duration": round(workout["duration_min"]),  # Get the duration of the workout
            "calories": workout["nf_calories"]  # Get the number of calories burnt
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params)
print("Your workouts have been added. You can view them in your spreadsheet.")
