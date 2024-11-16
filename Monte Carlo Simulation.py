import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Choose a stock symbol
stock_symbol = 'AAPL'

# Fetch stock data from Yahoo Finance
stock_data = yf.download(stock_symbol, start='2010-01-01', end='2023-11-16')

# Latest stock price (S0)
S0 = stock_data['Close'][-1]
print(f"Latest Stock Price (S0): {S0:.2f}")

# Calculate daily returns and statistical parameters
daily_returns = stock_data['Close'].pct_change().dropna()
mu_daily = daily_returns.mean()
sigma_daily = daily_returns.std()

# Annualize mean return (mu) and volatility (sigma)
mu = mu_daily * 252
sigma = sigma_daily * np.sqrt(252)

print(f"\nAnnualized Mean Return (µ): {mu:.5f}")
print(f"Annualized Standard Deviation (σ): {sigma:.5f}")

# Simulation parameters
T = 5  # time horizon (5 years)
dt = 1 / 252  # daily time step
N = int(T / dt)  # number of time steps
M = 1000  # number of simulations

# Initialize array for simulated price paths
simulations = np.zeros((M, N))

# Monte Carlo simulation
for i in range(M):
    Z = np.random.normal(0, 1, N)
    price_path = S0 * np.exp(np.cumsum((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z))
    simulations[i] = price_path

# Calculate the final returns for each simulation
final_returns = (simulations[:, -1] - S0) / S0

# Generate a colormap based on the final return values
norm = plt.Normalize(final_returns.min(), final_returns.max())
colors = cm.viridis(norm(final_returns))

# Plot all simulated paths
plt.figure(figsize=(10, 6))
for i in range(M):
    plt.plot(simulations[i], color=colors[i], alpha=0.1)
plt.title(f'Simulated Stock Price Paths for {stock_symbol} over 5 Years')
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.show()

# Calculate mean, 5th and 95th percentiles of simulated prices
mean_price = simulations.mean(axis=0)
percentile_5 = np.percentile(simulations, 5, axis=0)
percentile_95 = np.percentile(simulations, 95, axis=0)

# Plot mean path and confidence intervals
plt.figure(figsize=(10, 6))
plt.plot(mean_price, color='red', label='Mean Path')
plt.fill_between(range(N), percentile_5, percentile_95, color='gray', alpha=0.5, label='95% Confidence Interval')
plt.title(f'Stock Price Prediction with Confidence Interval for {stock_symbol}')
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price')
plt.legend()
plt.show()

# Predicted stock price at the 5-year mark (last day of simulation)
predicted_price_mean = mean_price[-1]
predicted_price_5th = percentile_5[-1]
predicted_price_95th = percentile_95[-1]

# Print the predicted future stock prices (mean and percentiles)
print("\nPredicted Future Stock Price (5 years from today):")
print(f"Mean Predicted Price: {predicted_price_mean:.2f}")
print(f"5th Percentile Price: {predicted_price_5th:.2f}")
print(f"95th Percentile Price: {predicted_price_95th:.2f}")
