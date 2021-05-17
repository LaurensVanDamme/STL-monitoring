from stlUtils import *

# New random example
# signal = [[0, 1, 2, 6, 10], [0, 0, -1, 1, 0], [0.0, -1.0, 0.5, -0.25, 0]]

# signal = [[0, 5, 6, 7, 8, 9], [0, 0, -1, -1, 0, 1], [0.0, -1.0, 0.0, 1.0, 1, 1]]
signal = [[0, 5, 6, 7, 8], [0, 0, -1, -1, 0], [0.0, -1.0, 0.0, 1.0, 0]]
# signal = [[0, 5, 6, 7], [0, 0, -1, -1], [0.0, -1.0, 0.0, 1.0]]
# signal = [[5, 6], [0, -1], [-1.0, 0.0]]
# signal = [[6, 7], [-1, -1], [0.0, 1.0]]
# signal = [[7, 8], [-1, 0], [1.0, 0.0]]
# signal = [[0, 1], [0, 0], [0.0, -1.0]]
a = 0
b = 2
t_0 = 0
# t_0 = float('inf')


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
    # temp = getPunctualIntersection(x, y)
    # if len(temp[0][0]) > 0:
        # values = [max(temp[0][1][i], temp[1][1][i]) for i in range(len(temp[0][0]))]
        # derivatives = [max(temp[0][2][i], temp[1][2][i]) for i in range(len(temp[0][0]))]
        # return [temp[0][0], values, derivatives]

    # return calculate_and_or(temp[0], temp[1], 'or')

    # else:  # No intersection -> combine
    #     raise Exception('This shouldn\'t happen - compute until - compute or - no intersection')
        # temp = [[], [], []]
        # indexes = sorted(x[0] + y[0])
        # i_x = 0
        # i_y = 0
        # for i in indexes:
        #     if i in x[0]:
        #         temp[0].append(i)
        #         temp[1].append(x[1][i_x])
        #         temp[2].append(x[2][i_x])
        #         i_x += 1
        #     else:
        #         temp[0].append(i)
        #         temp[1].append(y[1][i_y])
        #         temp[2].append(y[2][i_y])
        #         i_y += 1
        # return temp


def computeEventually(x, t_0=float('inf')):
    if t_0 == float('inf'):  # If no t_0 is given, use the smallest time step
        t_0 = x[0][0]
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
    M = {x[0][0]}

    z = [[], [], []]

    # while t + a < x[0][-2]:  # TODO: -2 should be -1 if 8 is not included (but now the rest depends on it)
    while t + a < x[0][-1]:
        # if i + 1 < len(x[0]) - 1 and len(M) > 0:  # TODO: -1 (first condition) shouldn't be there if 8 is not included (but now the rest depends on it)
        if i + 1 < len(x[0]) and len(M) > 0:
            t = min(min(M) - a, x[0][i+1] - b)
        elif len(M) == 0:
            t = x[0][i+1] - b
        else:
            t = min(M) - a

        if len(M) > 0 and t == min(M) - a:  # Delete from M
            # blub = min(M)
            M.remove(min(M))
            # new
            if s >= t_0:
                if len(M) == 0:
                    computed_or = y
                else:
                    yt_minM = getAffinePoint(x, min(M))

                    y_s_t = getSignalInterval(y, s, t)
                    y_constant = [y[0], [yt_minM] * len(y[0]), [0] * len(y[0])]
                    computed_or = computeOr(y_s_t, y_constant)

                i_s = computed_or[0].index(s)
                i_t = computed_or[0].index(t)

                for index in range(i_s, i_t + 1):
                    if computed_or[0][index] not in z[0]:
                        z[0].append(computed_or[0][index])
                        z[1].append(computed_or[1][index])
                        z[2].append(computed_or[2][index])
                    else:
                        i_z = z[0].index(computed_or[0][index])
                        z[1][i_z] = computed_or[1][index]
                        z[2][i_z] = computed_or[2][index]
            # end new
            s = t
            # s = blub

        if i + 1 < len(x[0]) and t == x[0][i+1] - b:  # Add to M
            # while len(M) != 0 and getAffinePoint(x, x[0][i+1] - b) >= getAffinePoint(x, max(M)):  # x[0][i+1] - b could be just t
            while len(M) != 0 and getAffinePoint(x, x[0][i+1]) >= getAffinePoint(x, max(M)):  # x[0][i+1] - b could be just t --> should be t + b (like now)
                M.remove(max(M))
            M.add(x[0][i+1])
            i += 1
        # elif i + 1 < len(x[0]) and len(M) == 0:
        #     if x[2][i] > 0:
        #         M.add(t + b)
        #     else:
        #         M.add(t + a + 1)

        # if s >= t_0:  # and s != t:  # TODO: check if M is empty and use formula with max (in test.py)
        #     if len(M) == 0:
        #         computed_or = y
        #     else:
        #         yt_minM = getAffinePoint(x, min(M))
        #
        #         y_s_t = getSignalInterval(y, s, t)
        #         y_constant = [y[0], [yt_minM] * len(y[0]), [0] * len(y[0])]
        #         computed_or = computeOr(y_s_t, y_constant)
        #
        #     i_s = computed_or[0].index(s)
        #     i_t = computed_or[0].index(t)
        #
        #     for index in range(i_s, i_t + 1):
        #         if computed_or[0][index] not in z[0]:
        #             z[0].append(computed_or[0][index])
        #             z[1].append(computed_or[1][index])
        #             z[2].append(computed_or[2][index])
        #         else:
        #             i_z = z[0].index(computed_or[0][index])
        #             z[1][i_z] = computed_or[1][index]
        #             z[2][i_z] = computed_or[2][index]

    return z


if __name__ == '__main__':
    print(computeEventually(signal, t_0))
