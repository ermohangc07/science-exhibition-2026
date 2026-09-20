"""
WEATHER PREDICTION PROJECT
============================
Uses the free Open-Meteo API (no API key needed!) to fetch real forecast
data, then applies simple RULE-BASED logic to make a "prediction" in
plain language. This keeps the coding manageable for class 8-9 while
still teaching real skills: API calls, JSON parsing, conditional logic.

Teaching sequence:
  STAGE 1: Fetch and print raw weather data for one city
  STAGE 2: Pull out the specific numbers we care about (temp, humidity, rain chance)
  STAGE 3: Write if/else rules to turn numbers into a plain-language prediction
  STAGE 4: Let the user type in any city name (geocoding lookup)
  STAGE 5 (stretch): Show a 3-day outlook instead of just today

Install requests first: pip install requests --break-system-packages
"""

import requests


def get_coordinates(city_name):
    """
    STAGE 4: Turn a city name typed by the user into latitude/longitude,
    using Open-Meteo's free geocoding API.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1}
    response = requests.get(url, params=params)
    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return None  # city not found

    result = data["results"][0]
    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


def get_weather_data(latitude, longitude):
    """
    STAGE 1 & 2: Fetch current weather + a few useful fields from Open-Meteo.
    No API key required - this is a free, open service.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "daily": "precipitation_probability_max,temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": 3,
    }
    response = requests.get(url, params=params)
    return response.json()


def make_prediction(temperature, humidity, rain_chance):
    """
    STAGE 3: This is the "brain" of the project - simple, explainable rules
    instead of a black-box model. Great for teaching if/elif/else logic.

    Encourage students to TUNE these thresholds themselves by comparing
    against real local weather over a few days.
    """
    messages = []

    if rain_chance >= 60:
        messages.append("High chance of rain today - carry an umbrella.")
    elif rain_chance >= 30:
        messages.append("Rain is possible later - keep an umbrella handy just in case.")
    else:
        messages.append("Low chance of rain - should stay dry.")

    if temperature >= 32:
        messages.append("It will feel hot - stay hydrated.")
    elif temperature <= 12:
        messages.append("It will feel cold - wear something warm.")
    else:
        messages.append("Temperature should feel comfortable.")

    if humidity >= 80 and temperature >= 25:
        messages.append("High humidity + warmth - expect it to feel muggy.")

    return " ".join(messages)


def print_forecast_summary(city_info, weather_data):
    current = weather_data["current"]
    daily = weather_data["daily"]

    print(f"\nWeather for {city_info['name']}, {city_info['country']}")
    print("-" * 40)
    print(f"Current temperature : {current['temperature_2m']} C")
    print(f"Current humidity    : {current['relative_humidity_2m']} %")
    print(f"Wind speed          : {current['wind_speed_10m']} km/h")

    today_rain_chance = daily["precipitation_probability_max"][0]
    prediction = make_prediction(
        temperature=current["temperature_2m"],
        humidity=current["relative_humidity_2m"],
        rain_chance=today_rain_chance,
    )
    print(f"\nToday's rain chance : {today_rain_chance}%")
    print(f"Prediction: {prediction}")

    # STAGE 5 (stretch): quick 3-day outlook
    print("\n3-Day Outlook:")
    for i in range(len(daily["temperature_2m_max"])):
        print(
            f"  Day {i + 1}: High {daily['temperature_2m_max'][i]}C / "
            f"Low {daily['temperature_2m_min'][i]}C, "
            f"Rain chance {daily['precipitation_probability_max'][i]}%"
        )


def main():
    city_name = input("Enter a city name: ").strip()

    city_info = get_coordinates(city_name)
    if city_info is None:
        print(f"Sorry, couldn't find a place called '{city_name}'. Try again.")
        return

    weather_data = get_weather_data(city_info["latitude"], city_info["longitude"])
    print_forecast_summary(city_info, weather_data)


if __name__ == "__main__":
    main()
