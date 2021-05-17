from stlUtils import *

signal = [[0, 5, 6, 7, 8], [0, 0, -1, -1, 0], [0.0, -1.0, 0.0, 1.0, 0]]
a = 0
b = 2

def shift(y, v):
    temp = [t - v for t in y[0]]  # Shift the signal
    i = 0
    while i < len(y[0]) and temp[i] < 0:  # Count how many values have a time step smaller than 0
        i += 1

    result = [temp[i:], y[1][i:], y[2][i:]]

    if i > len(y[0]) - 1:  # Add a point at time step 0 if the signal is completely shifted out
        result[0] = [0]
        result[1] = [getAffinePoint(y, v)]
        result[2] = [y[2][-1]]
    elif i > 0 and result[0][0] != 0 and y[2][i] != 0:  # Add a point at time step 0 if the derivative of the last deleted point isn't 0
        result[0] = [0] + result[0]
        result[1] = [getAffinePoint(y, v)] + result[1]
        result[2] = list(numpy.diff([result[1][0], result[1][1]]) / numpy.diff([result[0][0], result[0][1]])) + result[2]
    return result


def computeAnd(x, y):
    # x, y = getPunctualIntersection(x, y)
    # values = [min(x[1][i], y[1][i]) for i in range(len(x[0]))]
    # derivatives = [min(x[2][i], y[2][i]) for i in range(len(x[0]))]
    # return [x[0], values, derivatives]

    return calculate_and_or(x, y)


def computeOr(x, y):
    return calculate_and_or(x, y, 'or')


def computeEventually(x):
    y_a = shift(x, a)
    y_b = shift(x, b)
    y = computeOr(y_a, y_b)

    # TODO: no idea if this is needed
    # x, y = getPunctualIntersection(x, y)

    # i = 1
    # while i < len(x[0]) - 1:
    #     if x[1][i-1] == x[1][i] == x[1][i+1]:
    #         x[0].pop(i-1)
    #         x[1].pop(i-1)
    #         x[2].pop(i-1)
    #     else:
    #         i += 1
    # if x[1][0] == x[1][1]:
    #         x[0].pop(0)
    #         x[1].pop(0)
    #         x[2].pop(0)
    # if x[1][-2] == x[1][-1]:
    #         x[0].pop(-1)
    #         x[1].pop(-1)
    #         x[2].pop(-1)

    # for i in range(1, len(y[0])):
    #     if y[1][i-1] == y[1][i]:
    #         y[0].pop(i-1)
    #         y[1].pop(i-1)
    #         y[2].pop(i-1)

    # TODO: not sure if this is needed
    # # All time steps of x have to be present in y
    # # If they are not, we can be sure that the max of x and y is the value of x at that time step
    # for i in range(len(x[0])):
    #     if x[0][i] not in y[0]:
    #         y[0].append(x[0][i])
    #         y[1].append(x[1][i])
    #         y[2].append(x[2][i])
    # y = [list(p) for p in list(zip(*sorted(zip(y[0], y[1], y[2]))))]

    s = x[0][0] - b
    t = s
    i = 0
    M = [0]

    z = [[], [], []]

    while t + a < x[0][-2]:

        if len(M) > 0:
            M_empty = False
            if i + 1 >= len(x[0]):
                t = x[0][min(M)] - a  # Should never happen
            elif len(M) == 0:
                t = x[0][i + 1] - b  # Should never happen
            else:
                t = min(x[0][min(M)] - a, x[0][i + 1] - b)
            if len(M) > 0 and t == x[0][min(M)] - a:
                M.remove(min(M))
                s = t
            if i + 1 < len(x[0]) and t == x[0][i + 1] - b:
                while len(M) > 0 and getAffinePoint(x, x[0][i + 1] - b) >= x[1][max(M)]:  # x[0][i] - b could be just t
                    M.remove(max(M))
                M += [i + 1]
                i += 1
        else:
            M += [i + 1]
            M_empty = True
        # s != t because else we're working with an empty interval
        if s >= x[0][0] and s != t:  # TODO: check if M is empty
            if not M_empty:
                yt_minM = x[1][min(M)]
                y_s_t = [c[y[0].index(s):y[0].index(t)] for c in y]
                y_constant = [y[0], [yt_minM] * len(y[0]), [0] * len(y[0])]
                computed_or = computeOr(y_s_t, y_constant)
            else:
                computed_or = y

            i_s = computed_or[0].index(s)
            i_t = computed_or[0].index(t)

            for index in range(i_s, i_t):
                if computed_or[0][index] not in z[0]:
                    z[0].append(computed_or[0][index])
                    z[1].append(computed_or[1][index])
                    z[2].append(computed_or[2][index])
                else:
                    i_z = z[0].index(computed_or[0][index])
                    z[1][i_z] = computed_or[1][index]
                    z[2][i_z] = computed_or[2][index]
    return z

if __name__ == '__main__':
    print(computeEventually(signal))