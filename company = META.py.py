import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Define the company
company = "META"

# Download the data
print(f"Processing {company}...")
data = yf.download(company, period="3mo", interval="1d")

# Extract 'Close' prices
df = data['Close'].dropna()

# Create a DataFrame for features
df_features = pd.DataFrame()
df_features['Close'] = df

# Add lagged features
for i in range(1, 6):
    df_features[f'Close_Lag_{i}'] = df_features['Close'].shift(i)

# Drop rows with missing values
df_features = df_features.dropna()

# Define features and target
X = df_features.drop('Close', axis=1)
y = df_features['Close']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"{company} - Mean Squared Error: {mse:.2f}")
print(f"{company} - R² Score: {r2:.2f}")

# Plot the actual vs predicted prices
plt.figure(figsize=(14, 8))
plt.plot(y_test.index, y_test, label="Actual Price", color='blue')
plt.plot(y_test.index, y_pred, label="Predicted Price", color='red', linestyle='--')
plt.title(f'{company} - Actual vs Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
