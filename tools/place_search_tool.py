from langchain.tools import tool
import os
from dotenv import load_dotenv
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACE_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.places_search_tool_list = self._setup_tools()
        
    
    def _setup_tools(self) -> List:
        """Setup all tools for the place search tool"""
        @tool
        def search_attractions(place:str) -> str:
            """Search attraction of a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot fide the details due to {e}. \nFollowing are the attraction of {place}"
            
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"following are the restaurants of {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. n\Following are the restaurants of {place} as suggested by tavily: {tavily_result}"
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                activities_result = self.google_places_search.google_search_activity(place)
                if activities_result:
                    return f"following are the activities of {place} as suggested by google: {activities_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. n\Following are the activities of {place} as suggested by tavily: {tavily_result}"
            
            
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"following are the transportation of {place} as suggested by google: {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. n\Following are the transportation of {place} as suggested by tavily: {tavily_result}"
            
        return [search_attractions,search_restaurants,search_activities,search_transportation]
                