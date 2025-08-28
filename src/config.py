# Description: Handles configuration management, particularly for API keys.

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_groq_api_key():
    """
    Retrieves the Groq API key from environment variables.

    Returns:
        str: The Groq API key.
    
    Raises:
        ValueError: If the GROQ_API_KEY is not found in the environment.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in your .env file.")
    return api_key

def get_financial_data_api_key():
    """
    Retrieves the API key for the financial data provider from environment variables.
    
    Returns:
        str: The financial data API key.

    Raises:
        ValueError: If the FINANCIAL_DATA_API_KEY is not found in the environment.
    """
    api_key = os.getenv("FINANCIAL_DATA_API_KEY")
    if not api_key:
        raise ValueError("FINANCIAL_DATA_API_KEY not found in environment variables. Please set it in your .env file.")
    return api_key
