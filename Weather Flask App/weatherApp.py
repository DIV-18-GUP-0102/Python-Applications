from flask import Flask, jsonify
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__)

def get_weather_description(weather_id):
    # Mapping of weather IDs to their descriptions
    # Source: https://openweathermap.org/weather-conditions
    weather_descriptions = {
        200: "Thunderstorm with light rain",
        201: "Thunderstorm with rain",
        202: "Thunderstorm with heavy rain",
        210: "Light thunderstorm",
        211: "Thunderstorm",
        212: "Heavy thunderstorm",
        221: "Ragged thunderstorm",
        230: "Thunderstorm with light drizzle",
        231: "Thunderstorm with drizzle",
        232: "Thunderstorm with heavy drizzle",
        300: "Light intensity drizzle",
        301: "Drizzle",
        302: "Heavy intensity drizzle",
        310: "Light intensity drizzle rain",
        311: "Drizzle rain",
        312: "Heavy intensity drizzle rain",
        313: "Shower rain and drizzle",
        314: "Heavy shower rain and drizzle",
        321: "Shower drizzle",
        500: "Light rain",
        501: "Moderate rain",
        502: "Heavy intensity rain",
        503: "Very heavy rain",
        504: "Extreme rain",
        511: "Freezing rain",
        520: "Light intensity shower rain",
        521: "Shower rain",
        522: "Heavy intensity shower rain",
        531: "Ragged shower rain",
        600: "Light snow",
        601: "Snow",
        602: "Heavy snow",
        611: "Sleet",
        612: "Shower sleet",
        615: "Light rain and snow",
        616: "Rain and snow",
        620: "Light shower snow",
        621: "Shower snow",
        622: "Heavy shower snow",
        701: "Mist",
        711: "Smoke",
        721: "Haze",
        731: "Dust",
        741: "Fog",
        751: "Sand",
        761: "Dust",
        762: "Volcanic ash",
        771: "Squalls",
        781: "Tornado",
        800: "Clear sky",
        801: "Few clouds",
        802: "Scattered clouds",
        803: "Broken clouds",
        804: "Overcast clouds",
    }
    
    return weather_descriptions.get(weather_id, "Unknown")

@app.route('/city/<city_name>', methods=['GET'])
def get_weather(city_name):
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(city_name)
    if location:
        api_key = 'be8b22462bcfc479c070516ee37e2ef9'
        lat = location.latitude
        lon = location.longitude
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
        response = requests.get(url)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            temperature = weather_data['main']['temp']
            description = get_weather_description(weather_data['weather'][0]['id'])
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            sentences = [
                f"The current temperature is {temperature} Kelvin.",
                f"The weather condition is {description}.",
                f"The humidity is {humidity}%.",
                f"The wind speed is {wind_speed} meters per second."
            ]
            
            return jsonify({'sentences': sentences})
        else:
            return jsonify({'error': 'Failed to fetch weather data'})
    else:
        return jsonify({'error': 'City not found'})

if __name__ == '__main__':
    app.run(debug=True)
