# Stock Price Predictor

ML-powered stock price prediction using linear regression with historical data analysis.

## Features

- Real-time stock data fetching via Yahoo Finance
- Linear regression model with moving averages
- Interactive chart visualization
- Model accuracy display
- Clean, responsive UI

## Setup

1. Install dependencies:
```bash
pip install -r requirements_stock.txt
```

2. Run the application:
```bash
python stock_app.py
```

3. Open browser: http://localhost:5001

## Usage

1. Enter stock ticker (e.g., AAPL, GOOGL, MSFT)
2. Set prediction days (1-90)
3. Click "Predict" to see results

## Model Details

- Algorithm: Linear Regression
- Features: Days, 7-day MA, 30-day MA
- Training data: 1 year historical prices
- Preprocessing: MinMax scaling

## Files

- `stock_predictor.py`: ML model and data processing
- `stock_app.py`: Flask server
- `templates/stock.html`: UI template
- `static/stock.css`: Styling
- `static/stock.js`: Frontend logic
