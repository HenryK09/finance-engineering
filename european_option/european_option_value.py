import numpy as np
import scipy.stats as stat
import plotly.graph_objs as go
from plotly.offline import iplot


def get_european_option_value(S, K, T, r, sigma, option_type='call'):
    """
    Getting the value of a european option by using the
    Black-Scholes Option Formula.
    :param
        Variables
        S: underlying asset value
        T: time to maturity
        ---------------------------------
        Parameters
        K: initial value
        r: risk-free rate
        sigma: annualized volatility
        ---------------------------------
        option_type: 'call' or 'put'; str

    :return:
        the value of a european option
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        V = S * stat.norm.cdf(d1) - K * np.exp(-r * T) * stat.norm.cdf(d2)
    else:
        V = K * np.exp(-r * T) * stat.norm.cdf(-d2) - S * stat.norm.cdf(-d1)

    return V


def plot_european_option_surface(x, y, z, option_type):
    layout = go.Layout(title=f'{option_type}',
                       scene={'xaxis': {'title': 'Maturity'},
                              'yaxis': {'title': 'Spot Price'},
                              'zaxis': {'title': 'Option Price'}
                              }
                       )
    fig = go.Figure(data=go.Surface(x=x, y=y, z=z), layout=layout)
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))
    fig.update_layout(title=f'{option_type}', autosize=False,
                      width=700, height=500)
    fig.show()


def run_european_option(S, T, K, r, sigma, option_type='call'):
    S, T = np.meshgrid(S, T)

    option_val = get_european_option_value(S, K, T, r, sigma, option_type)

    plot_european_option_surface(T, S, option_val, f'{option_type} option')

    return option_val


def plot_option_value_with(K, r, sigma, maturity_period, option_type='call', xaxis='time to maturity'):
    data = []
    if xaxis == 'underlying asset price' or 'spot price':
        S = np.linspace(0, 200, 100)

        if maturity_period[-1] == 1:
            for i in range(maturity_period[0], 11, 2):
                T = i / 10
                Z = get_european_option_value(S, K, T, r, sigma, f'{option_type}')
                trace = go.Scatter(x=S, y=Z, name=('Maturity = ' + str(T)))
                data.append(trace)
        else:
            for i in range(maturity_period[0], maturity_period[-1] + 1, 2):
                T = i
                Z = get_european_option_value(S, K, T, r, sigma, f'{option_type}')
                trace = go.Scatter(x=S, y=Z, name=('Maturity = ' + str(T)))
                data.append(trace)

        layout = go.Layout(width=800, height=400, xaxis=dict(title='Spot Price'), yaxis=dict(title='Option Value'))
    else:
        for S in range(0, 201, 50):
            T = np.linspace(maturity_period[0], maturity_period[-1], 100)
            Z = get_european_option_value(S, K, T, r, sigma, f'{option_type}')
            trace = go.Scatter(x=T, y=Z, name=('Spot Price = ' + str(S)))
            data.append(trace)

        layout = go.Layout(width=800, height=400, xaxis=dict(title='Maturity'), yaxis=dict(title='Option Value'))

    fig = dict(data=data, layout=layout)

    iplot(fig)


if __name__ == '__main__':
    # Variables
    S = np.linspace(0, 200, 100)
    T = np.linspace(0, 1, 100)
    # Parameters
    K = 100
    r = 0.01
    sigma = 0.25

    # get option value and plot 3D surface
    call_option_val = run_european_option(S, T, K, r, sigma, 'call')
    put_option_val = run_european_option(S, T, K, r, sigma, 'put')

    # plot option value with underlying asset price(spot price)
    # Maturity 2 ~ 10
    plot_option_value_with(K, r, sigma, [2, 10], 'call', 'underlying asset price')
    plot_option_value_with(K, r, sigma, [2, 10], 'put', 'underlying asset price')
    # Maturity 0 ~ 1
    plot_option_value_with(K, r, sigma, [0, 1], 'call', 'underlying asset price')
    plot_option_value_with(K, r, sigma, [0, 1], 'put', 'underlying asset price')

    # plot option value with time to maturity(maturity)
    # Maturity 0 ~ 10
    plot_option_value_with(K, r, sigma, [0, 10], 'call', 'time to maturity')
    plot_option_value_with(K, r, sigma, [0, 10], 'put', 'time to maturity')
    # # Maturity 0 ~ 1
    plot_option_value_with(K, r, sigma, [0, 1], 'call', 'time to maturity')
    plot_option_value_with(K, r, sigma, [0, 1], 'put', 'time to maturity')
