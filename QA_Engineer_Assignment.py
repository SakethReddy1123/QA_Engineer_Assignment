import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return []

def get_weather_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["main"]["temp"]
    return None

def get_wind_speed_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["wind"]["speed"]
    return None

def get_pressure_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if entry["dt_txt"].startswith(date):
            return entry["main"]["pressure"]
    return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_weather_by_date(date)
            if temperature:
                print(f"Temperature on {date}: {temperature}°C")
            else:
                print("No data found for the specified date.")
        elif option == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data found for the specified date.")
        elif option == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(date)
            if pressure:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data found for the specified date.")
        elif option == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

main()