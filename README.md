# Monte-Carlo-Simulation

For this exercise, I created the Monte Carlo Simulation for a public stock over a 5-year horizon. 

The Monte Carlo Simulation models the expected returns of a stock in the future using historical returns and randomness at each new interval on the x-axis. At a new integer (x1->x2), there is a random influx in the compounded returns of the stock. The random returns are calculated using a normal distribution. To exclude outliers, only 95% of the return paths are kept (95% confidence level).

The annualized mean returns, the annualized mean volatility (standard deviation), the mean 5-year price, and the confidence level prices are printed in the terminal.

You can update the code to simulate any public company by updating the ticker, and you can update the price timeline by updating the date range. The historical price data may vary though depending on when the company was listed. Comparing companies may not be correct if their historical price timelines are different.
