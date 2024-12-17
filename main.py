class WeatherForecast:
    def __init__ (self): 
        self.weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

    def WeatherDataFetcher (self, cityname): # Returns Weather Data for input City Name
        print(f"Fetching weather data for {cityname}...")
        return self.weather_data.get(cityname, {})

class AppFunction:
    @staticmethod
    def WeatherDataParser (data):
        if not data:
            return "Weather data not available! Sorry, check back later."
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f'''Weather in {city} today is...
{temperature} degrees
Conditions are {condition}
Humidity is {humidity}%'''

class UserInterface:
    def __init__(self):
        self.ParseData = AppFunction()
        self.FetchData = WeatherForecast()

    def GetSimpleForecast (self, cityname):
        data = self.FetchData.WeatherDataFetcher(cityname)
        if not data:
            print(f"Weather data not available for {cityname}")
        else:
            print(f"The Temperature in {cityname} is {data["temperature"]}")

    def GetDetailedForecast (self, cityname):
        data = self.FetchData.WeatherDataFetcher(cityname)
        return self.ParseData.WeatherDataParser(data)
        
    def main(self):
        while True:
            try:
                cityname = input("Type the name of a city to get the weather forecast! Or, type 'exit' to quit: ")
                if cityname.lower() == 'exit':
                    break
                detailed_option = input("Do you want an extra detailed forecast? (yes/no): ").lower()
                if detailed_option == "yes":
                    forecast = self.GetDetailedForecast(cityname)
                else:
                    forecast = self.GetSimpleForecast(cityname)
                print(forecast)
            except ValueError as e:
                print(f"Invalid Entry: {e}")

if __name__ == "__main__":
    app = UserInterface()
    app.main()