import requests

print("🌤️ WEATHER APP 🌤️\n")

api ="6d5672238f7557007cef2f02f4ee387a"

def get_weather(city, api_key):
    """Get weather data for a city"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return data
        elif response.status_code == 401:
            print("❌ Invalid API key!")
            return None
        elif response.status_code == 404:
            print("❌ City not found!")
            return None
        else:
            print(f"❌ Error: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def display_weather(data):
    """Display weather information"""
    if data is None:
        return
    
    # Extract data INSIDE this function
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Print everything INSIDE this function
    print(f"\n{'='*40}")
    print(f"Weather in {city}, {country}")
    print(f"{'='*40}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Conditions: {description.capitalize()}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"{'='*40}\n")

# Main program
print("Get your FREE API key from: https://openweathermap.org/api\n")
api_key = input("Enter your API key: ").strip()

if not api_key:
    print("❌ API key required!")
    exit()

while True:
    city = input("\nEnter city name (or 'quit' to exit): ").strip()
    
    if city.lower() == "quit":
        print("👋 Goodbye!")
        break
    
    if not city:
        print("❌ Please enter a city name!")
        continue
    
    print("\n🔄 Fetching weather data...")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)