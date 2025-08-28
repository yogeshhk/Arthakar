# Description: Defines the custom tools for the Arthakar agent.
# This includes tools for fetching live market data, news, and parsing documents.

import requests
import json
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from config import get_financial_data_api_key

# --- MCP (Market & Community Pulse) Tools ---

@tool
def get_live_stock_price(ticker: str) -> str:
    """
    Fetches the latest stock price for a given ticker symbol.
    This is a placeholder and should be connected to a real-time data provider.
    """
    print(f"TOOL: Fetching live stock price for {ticker}...")
    # In a real implementation, you would use an API like Alpha Vantage or IEX Cloud.
    # For demonstration, we'll return a mock price.
    # This function can be expanded to return more details like volume, day high/low etc.
    return f"The current mock price for {ticker} is $150.75."

@tool
def get_financial_news(topic: str) -> str:
    """
    Searches for recent financial news about a specific topic or company.
    This uses a simple web scraping approach. A more robust solution would use a news API.
    """
    print(f"TOOL: Searching for news about {topic}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Using a simple search engine query
    url = f"https://www.google.com/search?q=financial+news+{topic}&tbm=nws"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        headlines = []
        # Find news articles in the search results
        for item in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd', limit=5):
            headlines.append(item.get_text())
            
        if not headlines:
            return f"No recent news found for {topic}."
            
        return "Recent News Headlines:\n- " + "\n- ".join(headlines)
    except requests.exceptions.RequestException as e:
        return f"Error fetching news: {e}"

# --- Docling (Document Parsing) Tools ---

@tool
def parse_document_text(file_path: str) -> str:
    """
    Parses text from a local document (e.g., a TXT file of a financial report).
    In a real-world scenario, this would handle PDFs using libraries like PyMuPDF.
    For this example, it reads a simple text file.
    """
    print(f"TOOL: Parsing document from {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # In a real implementation, you would perform NLP to structure this data.
        # For now, we return the first 1000 characters as a summary.
        return f"Successfully parsed document. Summary: {content[:1000]}..."
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except Exception as e:
        return f"An error occurred while parsing the document: {e}"
