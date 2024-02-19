# Flask Weather Forecast API

This Flask application provides a simple RESTful API for retrieving weather forecast data based on the provided city name.

## Prerequisites

1. Python 3.8
2. Flask
3. requests
4. geopy


## Usage
1.Run the Flask application:
```bash
python weatherApp.py
```
2. Send a GET request to retrieve weather forecast data for a specific city:
```bash
curl http://localhost:5000/city/{city_name}
````
Replace {city_name} with the name of the city for which you want to retrieve the weather forecast.
The API will return a JSON response with weather forecast information for the specified city, including temperature, weather condition, humidity, and wind speed.

## Example

### Request

```bash
curl http://localhost:5000/city/London
```

### Output
```json
{
    "sentences": [
        "The current temperature is 280.37 Kelvin.",
        "The weather condition is scattered clouds.",
        "The humidity is 70%.",
        "The wind speed is 2.24 meters per second."
    ]
}
```
![Weather Forecast](Weather Flask App\Readme.md.jpg)

## Configuration

1. Set the environment variable in your terminal before starting the Flask app to prevent exposing API keys.
``` bash
set OPENWEATHERMAP_API_KEY="Your_API_Key" 
```

## Built With
1. Flask - Python web framework
2. requests - HTTP library for making requests
3. geopy - Geocoding library for Python

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License