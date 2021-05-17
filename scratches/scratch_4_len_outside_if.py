from stlUtils import *

signal = [[0, 5, 6, 7, 8], [0, 0, -1, -1, 0], [0.0, -1.0, 0.0, 1.0, 0]]
a = 2
b = 4

def shift(y, v):
    temp = [t - v for t in y[0]]
    i = 0
    while i < len(y[0]) and temp[i] < 0:
        i += 1
    result = [temp[i:], y[1][i:], y[2][i:]]
    return result


def computeAnd(x, y):
    x, y = getPunctualIntersection(x, y)
    # values = [min(x[1][i], y[1][i]) for i in range(len(x[0]))]
    # derivatives = [min(x[2][i], y[2][i]) for i in range(len(x[0]))]
    # return [x[0], values, derivatives]

    return calculate_and_or(x, y)


def computeOr(x, y):
    temp = getPunctualIntersection(x, y)
    if len(temp[0][0]) > 0:
        # values = [max(temp[0][1][i], temp[1][1][i]) for i in range(len(temp[0][0]))]
        # derivatives = [max(temp[0][2][i], temp[1][2][i]) for i in range(len(temp[0][0]))]
        # return [temp[0][0], values, derivatives]

        return calculate_and_or(temp[0], temp[1], 'or')

    else:  # No intersection -> combine
        temp = [[], [], []]
        indexes = sorted(x[0] + y[0])
        i_x = 0
        i_y = 0
        for i in indexes:
            if i in x[0]:
                temp[0].append(i)
                temp[1].append(x[1][i_x])
                temp[2].append(x[2][i_x])
                i_x += 1
            else:
                temp[0].append(i)
                temp[1].append(y[1][i_y])
                temp[2].append(y[2][i_y])
                i_y += 1
        return temp


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

    while t + a < x[0][-1]:
        empty_M = False
        t = min(x[0][min(M)] - a, x[0][i+1] - b)
        if t == x[0][min(M)] - a:
            M.remove(min(M))
            s = t
        if t == x[0][i+1] - b:
            while len(M) != 0 and getAffinePoint(x, x[0][i+1] - b) >= x[1][max(M)]:  # x[0][i+1] - b could be just t
                M.remove(max(M))
            M += [i+1]
            i += 1
            # s != t because else we're working with an empty interval
        if len(M) == 0:
            M += [i+1]
            empty_M = True
        if s >= x[0][0]: # and s != t:  # TODO: check if M is empty and use formula with max (in test.py)
            if not empty_M:
                yt_minM = x[1][min(M) - 1]

                y_s_t = [c[y[0].index(s):y[0].index(t) + 1] for c in y]
                y_constant = [y[0], [yt_minM] * len(y[0]), [0] * len(y[0])]
                computed_or = computeOr(y_s_t, y_constant)
            else:
                computed_or = y


            i_s = computed_or[0].index(s)
            i_t = computed_or[0].index(t) + 1

            for index in range(i_s, i_t + 1):
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