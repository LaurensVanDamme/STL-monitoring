import pandas as pd
from numbers import Number
import numpy
import matplotlib.pyplot as plt
from stlUtils import *

currentPlot = 0
plotAmount = 11
fig, axs = plt.subplots(plotAmount, sharex=True, sharey=True)
fig.set_size_inches(cm2inch(15), cm2inch(plotAmount * 3))

semantic = 'boolean'

# blub_temp = [[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0.0, 1.0, 2.5, 3.5, 4.0, 5.0, 6.0, 7.155, 8.0, 9.0, 10.02, 11.0, 12.0], [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
blub_temp = [[[0.0, 1.0, 2.1, 3.0, 4.0, 5.0, 6.1, 7.0, 8.0, 8.2, 10.0, 11.0, 12.0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]], [[0.0, 1.0, 2.5, 3.5, 4.0, 5.0, 6.0, 7.155, 8.0, 9.0, 10.02, 11.0, 12.0], [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]]
result = list(getPunctualIntersection(blub_temp[0], blub_temp[1], semantic))

axs[currentPlot].step(blub_temp[1][0], blub_temp[1][1], 'g-', result[1][0], result[1][1], 'r-', where='post')
axs[currentPlot].set_title('s1')
currentPlot += 1
axs[currentPlot].step(blub_temp[0][0], blub_temp[0][1], 'g-', result[0][0], result[0][1], 'r-', where='post')
axs[currentPlot].set_title('s2')
currentPlot += 1

# Get the size for which all needed data is present
size = len(result[0][0])

# Get the values
a = 1
b = 2

until = []

# Get the true intervals of the signals
intervals_1 = []
intervals_2 = []
temp_1 = []
temp_2 = []
true_1 = False
true_2 = False
for i in range(size):
    if result[0][1][i] and not true_1:
        true_1 = True
        temp_1.append(result[0][0][i])
    elif not result[0][1][i] and true_1:
        true_1 = False
        # temp_1.append(result[0][0][i - 1])
        temp_1.append(result[0][0][i])
        intervals_1.append(temp_1)
        temp_1 = []

    if result[1][1][i] and not true_2:
        true_2 = True
        temp_2.append(result[1][0][i])
    elif not result[1][1][i] and true_2:
        true_2 = False
        # temp_2.append(result[1][0][i - 1])
        temp_2.append(result[1][0][i])
        intervals_2.append(temp_2)
        temp_2 = []
if true_1:
    temp_1.append(result[0][0][size - 1])
    intervals_1.append(temp_1)
if true_2:
    temp_2.append(result[1][0][size - 1])
    intervals_2.append(temp_2)

# Decompose and calculate the Until for the decompositions
intervals_until = []
for inter_1 in intervals_1:
    for inter_2 in intervals_2:
        # intersection = getBooleanIntersection(inter_1, inter_2)
        intersection = getBooleanIntersection(inter_1, inter_2)
        if intersection:
            axs[currentPlot].step(intersection, [1,0], 'r-', inter_1, [1,0], 'g:', inter_2, [1,0], 'b:', where='post')
            axs[currentPlot].set_title(f'intersection 1: (g) {inter_1} - (b) {inter_2} = (r) {intersection}')
            currentPlot += 1

            interval = [max(0, intersection[0] - b), min(size, intersection[1] - a)]

            if interval[0] > interval[1]:  # Interval doesn't exist
                axs[currentPlot].set_title(f'backshift: {interval}')
                currentPlot += 1
                continue

            axs[currentPlot].step(interval, [1,0], 'r-', where='post')
            axs[currentPlot].set_title(f'backshift: {interval}')
            currentPlot += 1

            intersection = getBooleanIntersection(interval, inter_1)
            if intersection:
                intervals_until.append(intersection)

                axs[currentPlot].step(intersection, [1,0], 'r-', inter_1, [1,0], 'g:', interval, [1,0], 'b:', where='post')
            else:
                axs[currentPlot].step(inter_1, [1, 0], 'g:', interval, [1, 0], 'b:', where='post')

            axs[currentPlot].set_title(f'intersection 2: (g) {inter_1} - (b) {interval} = (r) {intersection}')
            currentPlot += 1
        else:
            axs[currentPlot].step(inter_1, [1, 0], 'g:', inter_2, [1, 0], 'b:', where='post')
            axs[currentPlot].set_title(f'intersection 1: (g) {inter_1} - (b) {inter_2} = (r) {intersection}')
            currentPlot += 1

# Calculate the entire until
until += [result[1][0].copy()] + [[0] * size]
for inter in intervals_until:
    for t in inter:
        if t in until[0]:
            until[1][until[0].index(t)] = 1
        else:
            for i in range(len(until[0])):
                if until[0][i] > t:
                    until[0] = until[0][:i] + [t] + until[0][i:]
                    until[1] = until[1][:i] + [1] + until[1][i:]
                    break
    for i in range(until[0].index(inter[0]), until[0].index(inter[1])):
        until[1][i] = 1
    until[1][until[0].index(inter[1])] = 0
for i in reversed(range(len(until[0]))):
    if until[0][i] > result[0][0][-1] - b:
        if until[0][i - 1] < result[0][0][-1] - b:
            until[0][-1] = result[0][0][-1] - b
            until[1][-1] = until[1][-2]
        else:
            until[0].pop(-1)
            until[1].pop(-1)

axs[currentPlot].step(until[0], until[1], 'r-', where='post')
for inter in intervals_until:
    axs[currentPlot].step(inter, [1, 0], 'b:', where='post')
axs[currentPlot].set_title('until (r) - intervals (b)')
currentPlot += 1

plt.show()