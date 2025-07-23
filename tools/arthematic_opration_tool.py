import os
from dotenv import load_dotenv
load_dotenv()
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper


@tool
def multiply(a:int, b:int) -> int:
    """
    Multiply Two integers
    
    Args:
        a (int): The first integer
        b (int): The second integer
        
    Returns:
        int: The product of a and b
    """
    return a * b

@tool
def add(a:int, b:int) -> int:
    """Add two integers

    Args:
        a (int): The first integer
        b (int): The second intege

    Returns:
        int: The adition of a and b
    """
    return a + b

@tool
def currency_converter(from_curr:str, to_curr: str,value: float) -> float:
    os.environ['ALPHAVENTAGE_API_KEY'] = os.getenv("ALPHAVENTAGE_API_KEY")
    alpha_ventage = AlphaVantageAPIWrapper()
    response = alpha_ventage._get_exchange_rate(from_curr, to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']["5. Exchange Rate"]
    return value * float(exchange_rate)