import os
from typing import List
from dotenv import load_dotenv
from utils.weather_info import WeatherForcastTool
from langchain.tools import tool

class WeatherInfoTool:
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForcastTool(self.api_key)
        self.weather_tool_list = self._setup_tool()
    
    def _setup_tool(self) -> List:
        """Setup all tools for the weather forcast tool"""
        @tool
        def get_current_weather(city: str) -> str:
            """Get current weather for a city"""
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get("main",{}).get("temp", "N/A")
                desc = weather_data.get("weather",[{}])[0].get("description","N/A")
                
                return f"Current weather in {city}: {temp}O, {desc}"
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_weather_forcast(city:str) -> str:
            """Get weather forecast for a city"""
            forcast_data = self.weather_service.get_forcast_weather(city)
            if forcast_data and "list" in forcast_data:
                forcast_summary = []
                for i in range(len(forcast_data['list'])):
                    item = forcast_data['list'][i]
                    date = item['dt_txt'].split(" ")[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['descripton']
                    forcast_summary.append(f"{date}: {temp}: degree celcuis, {desc}")
                return f"Weather forcast for {city}:\n" + "\n".join(forcast_summary)
            return f"Could not fetch forcast for {city}"
        
        return [get_current_weather, get_weather_forcast]
