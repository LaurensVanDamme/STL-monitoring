import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def until_comparison():
    input = pd.read_csv('../signals/ex_decreasing_3000.csv')
    until = pd.read_csv('../signals/results/until_comparison.csv', index_col=False)

    plt.plot(input['x1'], '-', label='s1 = (((t - 3000)^2) * 0.00035) + 200')
    plt.plot(input['x2'], '-', label='s2 = -t + 3000')
    plt.xlabel('time step')
    plt.ylabel('signal')
    # plt.plot(until['s_t'], until['s'], '--', label='1st method')
    # plt.plot(until['e_t'], until['e'], 'r:', label='2nd method')
    plt.legend()
    plt.show()

    plt.plot(until['s_t'], until['s'], 'r-', label='1st method')
    plt.plot(until['e_t'], until['e'], 'g--', label='2nd method')
    plt.xlabel('time step')
    plt.ylabel('robustness')
    plt.legend()
    plt.show()


def bool_vs_quan():
    input_1 = pd.read_csv('../signals/results/angles_ep5_bool.csv', index_col=False)
    input_2 = pd.read_csv('../signals/results/angles_ep5_quan.csv', index_col=False)

    plt.plot(input_1['s'], '-', label='Validation (Boolean)')
    plt.plot(input_2['s'], '-', label='Robustness (Quantitative)')
    plt.xlabel('time step')
    plt.ylabel('value')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    until_comparison()
    # bool_vs_quan()

    # import os
    # f = os.walk('results')
    # print(list(f))