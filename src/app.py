from flask import Flask, request, jsonify
import requests
from geopy.geocoders import Nominatim
import os

app = Flask(__name__)

# NOTE: ideally, store this in an environment variable for security
# For this portfolio project, you can insert your key below.
API_KEY = "013b716d17cad1e8064a6a092a8cf06d" 

@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        # Parse the incoming JSON request (compatible with Dialogflow)
        data = request.get_json()
        
        # Extract city from Dialogflow parameters
        # Note: Ensure your Dialogflow agent uses the parameter name 'geo-city'
        source_city = data['queryResult']['parameters']['geo-city']
        
        # 1. Get Coordinates using Geopy
        geolocator = Nominatim(user_agent="WeatherBotApp")
        location = geolocator.geocode(source_city)
        
        if not location:
            return jsonify({"fulfillmentText": f"Sorry, I couldn't find the location: {source_city}."})
            
        lat = location.latitude
        lon = location.longitude
        
        # 2. Fetch Weather Data from OpenWeatherMap
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url)
        weather_data = response.json()
        
        # 3. Process Data
        # Convert Kelvin to Celsius
        current_temp = round(weather_data['main']['temp'] - 273.15, 2)
        min_temp = round(weather_data['main']['temp_min'] - 273.15, 2)
        max_temp = round(weather_data['main']['temp_max'] - 273.15, 2)
        
        condition = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        
        # 4. Construct Response
        response_text = (
            f"The weather in {source_city} is mainly {condition} ({description}). "
            f"Current temperature is {current_temp}°C, "
            f"ranging from {min_temp}°C to {max_temp}°C."
        )
        
        return jsonify({"fulfillmentText": response_text})

    except Exception as e:
        # Fallback error message
        return jsonify({"fulfillmentText": "Sorry, I encountered an error fetching the weather data."})

if __name__ == "__main__":
    app.run(debug=True)