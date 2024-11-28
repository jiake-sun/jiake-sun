import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# List of companies (stock symbols)
companies = ["AAPL", "MSFT", "GOOG", "TSLA", "AMZN", "META"]

# Create a figure and a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))  # 2 rows and 3 columns

# Flatten axes for easier indexing
axes = axes.flatten()

# Loop through each company and plot on a separate subplot
for i, company in enumerate(companies):
    # Download the data
    data = yf.download(company, period="3mo", interval="1d")
    
    # Skip if no data is found
    if data.empty:
        print(f"No data found for {company}. Skipping...")
        continue
    
    # Extract 'Close' prices
    df = data['Close'].dropna()

    # Plot the data on the corresponding subplot
    axes[i].plot(df.index, df, label=f"{company} Closing Price", color='blue')
    axes[i].set_title(f'{company} - Closing Prices')
    axes[i].set_xlabel('Date')
    axes[i].set_ylabel('Price (USD)')
    axes[i].legend()
    axes[i].grid(True)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the combined plot
plt.show()