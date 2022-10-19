import math
import numpy as np
import matplotlib.pyplot as plt


def get_white_noise(T, N):
    """
    :param
        t: total period
        n: number of trials
    :return:
        time; array
        white noise
    """
    dt = T / N
    sqrt_dt = math.sqrt(dt)

    t = np.array([i for i in np.arange(0, T, dt)])  # time array

    dX = np.random.randn(N) * sqrt_dt  # white noise

    return t, dX


def get_brownian_motion(dX):
    """
    :param dX: white noise
    :return: brownian motion
    """
    return np.cumsum(dX)


def plot_brownian_motion(t, dX, X):
    ax_w = plt.subplot(2, 1, 1)
    ax_w.set_title('White Noise')
    ax_w.plot(t, dX)

    ax_b = plt.subplot(2, 1, 2)
    ax_b.set_title('Brownian Motion')
    ax_b.plot(t, X)

    plt.subplots_adjust(hspace=0.4)
    plt.show()


if __name__ == '__main__':
    T = 1
    N = 10000

    t, dX = get_white_noise(T, N)
    X = get_brownian_motion(dX)

    plot_brownian_motion(t, dX, X)
