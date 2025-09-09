import requests

API_KEY = "e1e006bdf05ed6f1c0af136f1b7dea77" # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str) -> None:
    try:
        resp = requests.get(
            BASE_URL,
            params={"q": city, "appid": API_KEY, "units": "metric"},
            timeout=10
        )
        if resp.status_code == 401:
            print("❌ Invalid API key. Check your key on OpenWeatherMap.")
            return
        if resp.status_code == 404:
            print("❌ City not found. Check the spelling and try again.")
            return
        resp.raise_for_status()

        data = resp.json()
        name = data.get("name", city)
        main = data.get("main", {})
        weather_list = data.get("weather", [{}])
        wind = data.get("wind", {})

        temp = main.get("temp", "?")
        feels = main.get("feels_like", "?")
        humidity = main.get("humidity", "?")
        desc = weather_list[0].get("description", "?")
        wind_speed = wind.get("speed", "?")

        print(f"\n🌍 Weather in {name}:")
        print(f"🌡 Temperature: {temp}°C (feels like {feels}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁ Condition: {desc}")
        print(f"🌬 Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.Timeout:
        print("⚠ Request timed out. Check your internet.")
    except requests.exceptions.ConnectionError:
        print("⚠ Network error. Are you connected to the internet?")
    except requests.exceptions.RequestException as e:
        print("⚠ Unexpected error:", e)
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)
