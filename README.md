# Real---Time-Stock-Tracker
Live Data Pipeline: Python to Power BI Stock Dashboard

# Real-Time Stock Market Dashboard

This project is an end-to-end data pipeline that captures live stock market data and visualizes it in a dynamic Power BI dashboard. A Python script fetches real-time data for multiple US equities using the `yfinance` library and streams it to a Power BI cloud service, allowing for immediate visualization of market trends.

## Dashboard Preview
![Live Stock Dashboard Screenshot](Real%20Time%20stock%20Tracker.png)

## Key Features
- **Real-Time Data:** Fetches live market data with up-to-the-minute prices and volumes.
- **Multi-Stock Tracking:** Simultaneously tracks a user-defined list of 13 different stocks.
- **End-to-End Pipeline:** Fully automated data flow from the source (Yahoo Finance) to the final dashboard.
- **Interactive Visualization:** The Power BI dashboard includes slicers, cards, DAX measures (e.g., Moving Average), and multiple charts that update live.

## Tech Stack
- **Data Collection:** Python (`yfinance`, `requests`)
- **Data Visualization & BI:** Microsoft Power BI
- **Data Modeling:** DAX (for custom measures)

## Setup & Installation
To get this project running, you'll need Python and Power BI.

1.  **Clone the repository or download the `.py` file.**

2.  **Install the required Python libraries:**
    ```bash
    pip install yfinance requests pandas
    ```

3.  **Set up the Power BI Streaming Dataset:**
    - Log in to Power BI Service and create a new **Streaming dataset**.
    - Choose the **API** source type.
    - Define the data schema with the following fields: `datetime` (DateTime), `stock_symbol` (Text), `price` (Number), `volume` (Number).
    - **Crucially, enable "Historic data analysis"**.
    - Copy the **Push URL** provided by Power BI after creation.

4.  **Configure the Python Script:**
    - Open the `Real Time stock Tracker.py` script and paste your Power BI **Push URL** into the `POWER_BI_URL` variable.

## Usage
1.  Run the Python script from your terminal or IDLE:
    ```bash
    python "Real Time stock Tracker.py"
    ```

2.  Open your Power BI report file (or view it in the Power BI Service) and watch the live data update the visuals.

## Customization

### Adding More Stocks
You can easily customize the watchlist to track different or additional stocks.

1.  Open the `Real Time stock Tracker.py` script file.
2.  Locate the `STOCK_SYMBOLS` list near the top of the file.
3.  Add any valid Yahoo Finance ticker symbol to the list, ensuring it's in quotes and separated by a comma.

For example, to add Netflix (`NFLX`):

**Before:**
```python
STOCK_SYMBOLS = ["AAPL", "MSFT", "GOOGL", "TSLA"]
```

**After:**
```python
STOCK_SYMBOLS = ["AAPL", "MSFT", "GOOGL", "TSLA", "NFLX"]
```

