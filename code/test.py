import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    return response.json()

def main():
    api_key = "your_api_key_here"  # Replace with your actual API key
    city = "San Antonio"
    weather_data = get_weather(api_key, city)
    
    if weather_data["cod"] != "404":
        main_weather = weather_data["main"]
        temperature = main_weather["temp"]
        pressure = main_weather["pressure"]
        
        humidity = main_weather["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        
        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Weather description: {weather_description}")
    else:
        print("City Not Found")

if __name__ == "__main__":
    main()

    