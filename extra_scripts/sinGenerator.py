import pandas as pd
import math
import matplotlib.pyplot as plt
import random

# To create input signals
if __name__ == "__main__":
    amount = 9000
    omega = 2 * math.pi * 1/78.5  # f = 1/78.5 ; T = 78.5 -> 1 cycle every 78.5 time steps
    x1 = []
    for i in range(amount):
        # x1.append(round(math.sin(i * omega), 10))
        x1.append((((i - 9000)**2)*0.00015) + 200)

    x2 = []
    for i in range(amount):
        # x2.append(round(math.cos(i * omega), 10))
        x2.append(-i+9000)

    # x2 = [0,0,0,0,0]
    # # indexes = []
    # theta = 0
    # for i in range(5, amount):
    #     theta = random.uniform(-0.5, 0.5)
    #     delay = random.uniform(3, 5)
    #     # indexes.append(i + delay)
    #     x2.append(round(math.sin((i - delay) * omega) + theta, 10))


    df = pd.DataFrame(list(zip(x1, x2)), columns=['x1', 'x2'])
    df.to_csv('ex_decreasing_9000.csv')

    plt.plot(x1, '-')
    plt.plot(x2, '-')
    plt.show()