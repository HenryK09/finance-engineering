import numpy as np
import matplotlib.pyplot as plt


def get_risk_free_value(init_val, r, t):
    """
    get risk-free price
    :param
        init_val: initial investment
        r: risk-free rate
        t: time to investment
    :return:
        risk-free value
    """
    return init_val * np.exp(r * t)


def plot_risk_free_asset(t, v):
    plt.plot(t, v)
    plt.title('Risk-free Asset')
    plt.show()


if __name__ == '__main__':
    t = np.array([x for x in np.arange(0, 100, 0.1)])
    rf_val = get_risk_free_value(init_val=100, r=0.04, t=t)
    plot_risk_free_asset(t, rf_val)

