import numpy as np
import matplotlib.pyplot as plt


def conduct_monte_carlo_simulation(S0, mu, sigma, T, D, N):
    dt = T / D  # Annualized Measure of 1 Day

    # create an empty array and fill initial value
    S = np.zeros((D + 1, N))
    S[0] = S0

    for t in range(1, D + 1):
        S[t] = S[t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.randn(N))

    return S


def plot_graph(S):
    plt.plot(S[:, :10000])
    plt.title('Monte Carlo Simulaion')
    plt.xlabel('day')
    plt.ylabel('price')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    S0 = 100  # Initial Price
    mu = 0.1  # Drift
    sigma = 0.23  # Volatility
    T = 1.0  # Time to Maturity
    D = 252  # Trading Days in 1 Year
    N = 10000  # Number of Trials

    S = conduct_monte_carlo_simulation(S0, mu, sigma, T, D, N)
    plot_graph(S)
