import numpy as np
import matplotlib.pyplot as plt


def get_risky_asset_price(S0, mu, sigma, T, N):
    St = S0 * np.exp((mu - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * np.random.randn(N))
    return St


def plot_risky_asset_histogram(St):
    print(len(St))
    plt.hist(St, bins=50)
    plt.title('Risky Asset Price Distribution')
    plt.xlabel('price at maturity')
    plt.ylabel('frequency')
    plt.show()


if __name__ == '__main__':
    S0 = 100  # Initial Price
    mu = 0.1  # Drift
    sigma = 0.23  # Volatility
    T = 1  # Time to Maturity
    N = 10000  # Number of Trials

    St = get_risky_asset_price(S0, mu, sigma, T, N)
    plot_risky_asset_histogram(St)