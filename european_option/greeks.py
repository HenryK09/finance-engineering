import numpy as np
import scipy.stats as stat
import plotly.graph_objs as go
from plotly.offline import iplot


def get_d(S, K, r, T, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * (sigma ** 2)) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * T ** 0.5
    return d1, d2


def get_delta(option_type, d1):
    if option_type == 'call':
        return stat.norm.cdf(d1)
    else:
        return stat.norm.cdf(d1) - 1


def get_theta(option_type, d1, d2):
    if option_type == 'call':
        option_type = 1
    else:
        option_type = -1

    return (-sigma * S * stat.norm.pdf(d1)) / (2 * np.sqrt(T)) - option_type * (
            r * K * np.exp(-r * T) * stat.norm.cdf(option_type * d2))


def get_gamma(d1):
    return stat.norm.pdf(d1) / (sigma * S * np.sqrt(T))


def plot_greeks_surface(greek_name, T, S, greek_val, n2, start_t, end_t, start_s, end_s):
    trace = go.Surface(x=T, y=S, z=greek_val, colorscale='Jet', opacity=0.8,
                       contours_x=dict(show=True, color='black', start=start_t, end=end_t, size=(end_t - start_t) / n2,
                                       project_x=True),
                       contours_y=dict(show=True, color='black', start=start_s, end=end_s, size=(end_s - start_s) / n2,
                                       project_y=True)
                       )
    data = [trace]
    layout = go.Layout(title=f'{greek_name} Surface',
                       scene={'xaxis': {'title': 'Maturity'},
                              'yaxis': {'title': 'Spot Price'},
                              'zaxis': {'title': f'{greek_name}'}
                              },
                       width=800, height=800, autosize=False,
                       margin=dict(pad=0)
                       )
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)


if __name__ == '__main__':
    K = 100  # strike price
    r = 0.01  # risk-free rate
    sigma = 0.25  # volatility

    n1 = 100  # number of steps for x, y axis
    n2 = 50  # number of contour lines
    start_t = 0.000001  # start value of maturity
    end_t = 1  # end value of maturity
    start_s = 0.000001  # start value of underlying asset price
    end_s = 200  # end value of underlying asset price

    T = np.linspace(start_t, end_t, n1)  # time to maturity
    S = np.linspace(start_s, end_s, n1)  # underlying asset price
    T, S = np.meshgrid(T, S)

    d1, d2 = get_d(S, K, r, T, sigma)

    # get Delta and plot Delta Surface
    call_delta = get_delta('call', d1)
    put_delta = get_delta('put', d1)

    plot_greeks_surface('Call Delta', T, S, call_delta, n2, start_t, end_t, start_s, end_s)
    plot_greeks_surface('Put Delta', T, S, put_delta, n2, start_t, end_t, start_s, end_s)

    # get Theta and plot Theta Surface
    call_theta = get_theta('call', d1, d2)
    put_theta = get_theta('put', d1, d2)

    plot_greeks_surface('Call Theta', T, S, call_theta, n2, start_t, end_t, start_s, end_s)
    plot_greeks_surface('Put Theta', T, S, put_theta, n2, start_t, end_t, start_s, end_s)

    # get Gamma and plot Gamma Surface
    call_gamma = get_gamma(d1)
    put_gamma = get_gamma(d1)

    plot_greeks_surface('Call Gamma', T, S, call_gamma, n2, start_t, end_t, start_s, end_s)
    plot_greeks_surface('Put Gamma', T, S, put_gamma, n2, start_t, end_t, start_s, end_s)
