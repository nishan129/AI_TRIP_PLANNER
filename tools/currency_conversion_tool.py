import os
from dotenv import load_dotenv
from langchain.tools import tool
from utils.currency_convertor import CurrencyConvertor
class CurrencyConvetorTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXChANGE_RATE_API_KEY")
        self.curracy_service = CurrencyConvertor(self.api_key)
        self.currency_convertor_tool_list = self._setup_tools()
    
    def _setup_tools(self):
        """Setup all tools for the currency converter tool"""
        @tool
        def convert_currency(amount:float, from_currency:str, to_currency:str):
            """Convert amount from one currecy to another"""
            return self.curracy_service.convert(amount,from_currency,to_currency)
        return [convert_currency]
    