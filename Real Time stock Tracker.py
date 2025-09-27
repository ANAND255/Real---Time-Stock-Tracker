import requests
import json
import time
from datetime import datetime
import yfinance as yf 


POWER_BI_URL = "https://api.powerbi.com/beta/e14e73eb-5251-4388-8d67-8f9f2e2d5a46/datasets/9077b2dc-45f3-49e5-831c-465a8b20ad44/rows?experience=power-bi&key=0WxGE3PFsaVxpCbfsujJX5P%2F5v1ICh0DAKN7m90HiBaFdGXeLPbkNRpsgDhWfb1SzOP4f%2B%2BLdxohirvB9QJgzg%3D%3D"


STOCK_SYMBOLS = [
    "AAPL",  # Apple
    "MSFT",  # Microsoft
    "GOOGL", # Alphabet (Google)
    "AMZN",  # Amazon
    "NVDA",  # NVIDIA
    "TSLA",  # Tesla
    "META",  # Meta Platforms
    "JPM",   # JPMorgan Chase
    "JNJ",   # Johnson & Johnson
    "WMT",   # Walmart
    "V",     # Visa
    "PG",    # Procter & Gamble
    "AMD"    # Advanced Micro Devices
]



def get_stock_data(symbol):
    """Fetches the latest stock data using the yfinance library."""
    try:
        ticker = yf.Ticker(symbol)
        
        hist = ticker.history(period="1d", interval="1m")
        
        
        if hist.empty:
            print(f"No data returned for {symbol}. Market might be closed or data unavailable.")
            return None
            
        
        latest_data = hist.iloc[-1]
        
        stock_payload = [{
            "datetime": datetime.now().isoformat(),
            "stock_symbol": symbol,
            "price": float(latest_data["Close"]),
            "volume": int(latest_data["Volume"])
        }]
        
        print(f"Successfully fetched data: {stock_payload}")
        return stock_payload
        
    except Exception as e:
        print(f"An error occurred with yfinance for {symbol}: {e}")
        return None

def push_to_power_bi(payload):
    """Pushes the formatted data to the Power BI streaming dataset."""
    if not payload:
        print("No payload to push.")
        return
    try:
        response = requests.post(POWER_BI_URL, json=payload)
        response.raise_for_status()
        print(f"Data successfully pushed to Power BI (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Error pushing data to Power BI: {e}")



if __name__ == "__main__":
    while True:
        for symbol in STOCK_SYMBOLS:
            print(f"--- Fetching data for {symbol} ---")
            stock_data_payload = get_stock_data(symbol)
            push_to_power_bi(stock_data_payload)
            
            time.sleep(15)
