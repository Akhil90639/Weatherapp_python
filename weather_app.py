import requests

def get_weather_data(api_key, city_name):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Units can be changed to imperial if desired
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    return data

def get_temperature(data, target_date):
    for entry in data["list"]:
        if target_date:
            return entry["main"]["temp"]
    return None

def get_wind_speed(data, target_date):
    for entry in data["list"]:
        if target_date:
            return entry["wind"]["speed"]
    return None

def get_pressure(data, target_date):
    for entry in data["list"]:
        if target_date:
            return entry["main"]["pressure"]
    return None

def main():
    api_key = "d713f891ab665a0fa9d6bf1fd6c2a4a7"  # Replace with your actual API key
    city_name = input("Enter city name: ")
    
    while True:
        print("\nSelect an option:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        
        option = input("Enter option: ")
        
        if option == "1":
            target_date = input("Enter date (YYYY-MM-DD): ")
            data = get_weather_data(api_key, city_name)
            temperature = get_temperature(data, target_date)
            if temperature is not None:
                print(f"Temperature: {temperature}°C")
            else:
                print("Temperature data not found for the provided date.")
        
        elif option == "2":
            target_date = input("Enter date and time (YYYY-MM-DD): ")
            data = get_weather_data(api_key, city_name)
            wind_speed = get_wind_speed(data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed: {wind_speed} m/s")
            else:
                print("Wind speed data not found for the provided date.")
        
        elif option == "3":
            target_date = input("Enter date (YYYY-MM-DD): ")
            data = get_weather_data(api_key, city_name)
            pressure = get_pressure(data, target_date)
            if pressure is not None:
                print(f"Pressure: {pressure} hPa")
            else:
                print("Pressure data not found for the provided date.")
        
        elif option == "0":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
     main()

