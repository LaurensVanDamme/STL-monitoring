import numpy


def cm2inch(value):
    return value/2.54

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# def getSamplingPointsIntersection(s1, s2):
#     loop_range = len(s1)
#     i_1 = 0
#     i_2 = 0
#     s1_pop = []
#     s2_pop = []
#     while i_1 < len(s1[0]) and i_2 < len(s2[0]):
#         if s1[0][i_1] == s2[0][i_2]:
#             i_1 += 1
#             i_2 += 1
#         elif s1[0][i_1] < s2[0][i_2]:
#             s1_pop.append(i_1)
#             i_1 += 1
#         elif s1[0][i_1] > s2[0][i_2]:
#             s2_pop.append(i_2)
#             i_2 += 1
#     for i in range(i_1, len(s1[0])):
#         s1_pop.append(i)
#     for i in range(i_2, len(s2[0])):
#         s2_pop.append(i)
#     for index in reversed(s1_pop):
#         for i in range(loop_range):
#             s1[i].pop(index)
#     for index in reversed(s2_pop):
#         for i in range(loop_range):
#             s2[i].pop(index)
#     return s1, s2


def getAffinePoint(signal, t):
    if t > max(signal[0]):
        return signal[1][-1] + signal[2][-1] * (t - signal[0][-1])
    i = 0
    while signal[0][i] <= t:
        if signal[0][i] == t:
            return signal[1][i]
        i += 1
    if i == 0:
        return signal[1][i]
    elif i >= len(signal[0]):
        return signal[1][-1]
    else:
        return float(signal[1][i] - signal[1][i - 1]) / float(signal[0][i] - signal[0][i - 1]) * float(t - signal[0][i - 1]) + signal[1][i - 1]


def getAffineDerivative(signal, t):
    if t < signal[0][0]:
        return 0
    for i in range(len(signal[0])):
        if t < signal[0][i]:
            return signal[2][i - 1]


def getSignalInterval(signal, a, b, half_open=False):
    if a > signal[0][-1]:
        return [[a, b + 1], [signal[1][-1]] * 2, [0, 0]]

    x = a
    if a not in signal[0]:
        for t in signal[0]:
            if t > a:
                x = t
                break

    if a == b:
        if half_open:
            return [[], [], []]
        else:
            if signal[0].index(x) == 0:
                derivative = 0
            else:
                derivative = signal[2][signal[0].index(x) - 1]
            return [[a], [getAffinePoint(signal, a)], [derivative]]

    y = b
    if b not in signal[0]:
        for i in reversed(range(len(signal[0]))):
            if signal[0][i] < b:
                if half_open:
                    y = signal[0][i+1]
                else:
                    y = signal[0][i]
                break
        if y == b:
            y = signal[0][0]

    if half_open:
        result = [c[signal[0].index(x):signal[0].index(y)] for c in signal]
    else:
        result = [c[signal[0].index(x):signal[0].index(y) + 1] for c in signal]

    if x != a:
        result[0] = [a] + result[0]
        result[1] = [getAffinePoint(signal, a)] + result[1]

    if y != b and not half_open:
        result[0] += [b]
        result[1] += [getAffinePoint(signal, b)]
        result[2] += list(numpy.diff([result[1][-2], result[1][-1]]) / numpy.diff([result[0][-2], result[0][-1]]))

    if x != a:  # positioned here if there wasn't a second value yet
        result[2] = list(numpy.diff([result[1][0], result[1][1]]) / numpy.diff([result[0][0], result[0][1]])) + result[2]

    return result


def getPunctualIntersection(s1, s2, semantic='quantitative'):
    if len(s1[0]) == 0 or len(s2[0]) == 0:
        return [[], [], []]
    if semantic == 'boolean':
        s1 += [[0] * len(s1[0])]
        s2 += [[0] * len(s2[0])]
    i_1 = 0
    i_2 = 0
    start = max(min(s1[0]), min(s2[0]))  # The start of punctual intersection
    end = min(max(s1[0]), max(s2[0]))  # The end of punctual intersection

    # Find how many time steps are passed in each signal to get to start
    # (Only one signal of two has defined values before start)
    while i_1 < len(s1[0]) and s1[0][i_1] < start:
        i_1 += 1
    while i_2 < len(s2[0]) and s2[0][i_2] < start:
        i_2 += 1

    temp_1 = [[], [], []]
    temp_2 = [[], [], []]

    # TODO: shouldn't this and the addition at the end be skipped? -> what isn't know, isn't know
    # Add the values at the time steps till start
    # We assume that the signals are constant (derivative = 0) before their first know value
    for i in range(i_1):
        temp_1[0].append(s1[0][i])
        temp_1[1].append(s1[1][i])
        temp_1[2].append(s1[2][i])
        # Add a value at the time step that is defined in s1 and not in s2
        temp_2[0].append(s1[0][i])
        temp_2[1].append(s2[1][0])
        temp_2[2].append(0)
    for i in range(i_2):
        # Add a value at the time step that is defined in s2 and not in s1
        temp_1[0].append(s2[0][i])
        temp_1[1].append(s1[1][0])
        temp_1[2].append(0)
        temp_2[0].append(s2[0][i])
        temp_2[1].append(s2[1][i])
        temp_2[2].append(s2[2][i])


    while i_1 < len(s1[0]) and i_2 < len(s2[0]) and (s1[0][i_1] <= end or s2[0][i_2] <= end):
        if s1[0][i_1] == s2[0][i_2]:  # Both signals are defined at the time step
            temp_1[0].append(s1[0][i_1])
            temp_1[1].append(s1[1][i_1])
            temp_1[2].append(s1[2][i_1])
            temp_2[0].append(s2[0][i_2])
            temp_2[1].append(s2[1][i_2])
            temp_2[2].append(s2[2][i_2])
            i_1 += 1
            i_2 += 1
        elif s1[0][i_1] < s2[0][i_2]:  # s2 is not defined at the i_1 time step where s1 is defined
            temp_2[0].append(s1[0][i_1])
            if semantic == 'quantitative':
                temp_2[1].append((s2[1][i_2] - s2[1][i_2 - 1]) / (s2[0][i_2] - s2[0][i_2 - 1]) * (s1[0][i_1] - s2[0][i_2 - 1]) + s2[1][i_2 - 1])
            else:
                temp_2[1].append(s2[1][i_2 - 1])
            temp_2[2].append(s2[2][i_2 - 1])
            temp_1[0].append(s1[0][i_1])
            temp_1[1].append(s1[1][i_1])
            temp_1[2].append(s1[2][i_1])
            i_1 += 1
        elif s1[0][i_1] > s2[0][i_2]:  # s1 is not defined at the i_2 time step where s2 is defined
            temp_1[0].append(s2[0][i_2])
            if semantic == 'quantitative':
                temp_1[1].append((s1[1][i_1] - s1[1][i_1 - 1]) / (s1[0][i_1] - s1[0][i_1 - 1]) * (s2[0][i_2] - s1[0][i_1 - 1]) + s1[1][i_1 - 1])
            else:
                temp_1[1].append(s1[1][i_1 - 1])
            temp_1[2].append(s1[2][i_1 - 1])
            temp_2[0].append(s2[0][i_2])
            temp_2[1].append(s2[1][i_2])
            temp_2[2].append(s2[2][i_2])
            i_2 += 1
        else:
            raise Exception("Something went wrong in getPunctualIntersection")

    # Fill the values from end on
    # We assume that the signals are have a constant derivative from their last known value (should always be 0)
    for i in range(i_1, len(s1[0])):
        temp_1[0].append(s1[0][i])
        temp_1[1].append(s1[1][i])
        temp_1[2].append(s1[2][i])
        temp_2[0].append(s1[0][i])
        temp_2[1].append(temp_2[1][-1] + (temp_2[0][-1] - temp_2[0][-2]) * temp_2[2][-1])
        temp_2[2].append(temp_2[2][-1])
    for i in range(i_2, len(s2[0])):
        temp_1[0].append(s2[0][i])
        temp_1[1].append(temp_1[1][-1] + (temp_1[0][-1] - temp_1[0][-2]) * temp_1[2][-1])
        temp_1[2].append(temp_1[2][-1])
        temp_2[0].append(s2[0][i])
        temp_2[1].append(s2[1][i])
        temp_2[2].append(s2[2][i])

    return temp_1, temp_2


def getBooleanIntersection(a, b):
    intersection =  [max(a[0], b[0]), min([a[-1], b[-1]])]
    if intersection[0] > intersection[1]:
        return False
    else:
        return intersection
    # Seems a stupid function to me, totally unnecessary and not well made
    # a_indexes = []
    # for i in range(a[0], a[1] + 1):
    #     a_indexes.append(i)
    # b_indexes = []
    # for i in range(b[0], b[1] + 1):
    #     b_indexes.append(i)
    # intersection = [value for value in a_indexes if value in b_indexes]
    # if len(intersection) > 0:
    #     return [min(intersection), max(intersection)]
    # else:
    #     return False



# x and y are signals in the form of [t, x, dx]
# operator is one of the following: 'and' or 'or'
def calculate_and_or(x, y, operator='and'):
    x, y = getPunctualIntersection(x, y)
    OPERATORS = {'or': lambda x, y: x > y,
                 'and': lambda x, y: x < y}
    temp = [[], [], []]
    last = None  # Indicating which signal had the last max/min
    for i in range(len(x[0])):
        if x[1][i] == y[1][i]:
            last = None
            temp[0].append(x[0][i])
            temp[1].append(x[1][i])
            temp[2].append(x[2][i])
        elif OPERATORS[operator](x[1][i], y[1][i]):
            if last == 'y':
                inter = line_intersection([[x[0][i - 1], x[1][i - 1]], [x[0][i], x[1][i]]],
                                          [[y[0][i - 1], y[1][i - 1]], [y[0][i], y[1][i]]])
                temp[0].append(inter[0])
                temp[1].append(inter[1])
                temp[2].append(x[2][i - 1])
            last = 'x'
            temp[0].append(x[0][i])
            temp[1].append(x[1][i])
            temp[2].append(x[2][i])
        elif OPERATORS[operator](y[1][i], x[1][i]):
            if last == 'x':
                inter = line_intersection([[x[0][i - 1], x[1][i - 1]], [x[0][i], x[1][i]]],
                                          [[y[0][i - 1], y[1][i - 1]], [y[0][i], y[1][i]]])
                temp[0].append(inter[0])
                temp[1].append(inter[1])
                temp[2].append(y[2][i - 1])
            last = 'y'
            temp[0].append(y[0][i])
            temp[1].append(y[1][i])
            temp[2].append(y[2][i])
    return temp
