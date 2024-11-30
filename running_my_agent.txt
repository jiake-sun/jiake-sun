   # fetch_data.py — Fetch stock data using yfinance 
import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch stock data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data
    # predict.py — Predict stock prices using a simple moving average (SMA)

def make_prediction(stock_data):

    # Simple moving average (SMA) prediction
    stock_data['SMA'] = stock_data['Close'].rolling(window=10).mean()  # 10-day SMA
    return stock_data['SMA']
    # plot_results.py — Plot the stock prices and predictions
import matplotlib.pyplot as plt

def plot_prediction(stock_data, predictions):
    # Plotting actual stock prices and predicted SMA
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Close'], label="Actual Close Price", color='blue')
    plt.plot(predictions, label="Predicted SMA", linestyle='--', color='orange')
    plt.title("Stock Price Prediction with Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()
    # greeting_message.py — A fun greeting message

def greet():
    print("""
    🏦 Welcome to your Stock Market Agent! 
    Let's fetch the latest stock data, make some predictions, and see how well we can forecast the market!
    Your financial wizardry starts now! """)

   # Define the greeting message1()
def greeting_message1(): 
    print("Hey there, you stock market sorcerer! 🪄📈 "
          "Let us steer this ship toward wealth. 🌊💰")
    greeting_message1

# greeting_message1()
   # print("Hey there, you stock market sorcerer! 🪄📈 "
          "Let's fetch the latest stock data, make some predictions, "
          "and see how well we can forecast the market!"

#""I hope your crystal ball is working because, frankly,I am having a hard time telling whether today  market is going to make me rich or just make me need a drink "" 
#""Let us steer this ship toward wealth  "")

   # Print the greeting message1
    print(greeting_message1)
   
    # main.py — The main script to run everything
    from greeting_message import greet
    from fetch_data import fetch_stock_data
    from predict import make_prediction
    from plot_results import plot_prediction

def main():
    # Display greeting
    greet()

    # Fetch stock data for a given ticker (e.g., "AAPL" for Apple)
    ticker = "AAPL"
    stock_data = fetch_stock_data(ticker, "2023-01-01", "2024-01-01")
    
    # Make a prediction (simple moving average)
    predictions = make_prediction(stock_data)
    
    # Plot results
    plot_prediction(stock_data, predictions)

if __name__ == "__main__":
    main()
