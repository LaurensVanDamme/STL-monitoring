signal = [[0, 5, 6, 7, 8], [0, 0, -1, -1, 0], [0.0, -1.0, 0.0, 1.0, 0]]

a = 0
b = 2

def getSamplingPointsIntersection(s1, s2):
    loop_range = len(s1)
    i_1 = 0
    i_2 = 0
    s1_pop = []
    s2_pop = []
    while i_1 < len(s1[0]) and i_2 < len(s2[0]):
        if s1[0][i_1] == s2[0][i_2]:
            i_1 += 1
            i_2 += 1
        elif s1[0][i_1] < s2[0][i_2]:
            s1_pop.append(i_1)
            i_1 += 1
        elif s1[0][i_1] > s2[0][i_2]:
            s2_pop.append(i_2)
            i_2 += 1
    for i in range(i_1, len(s1[0])):
        s1_pop.append(i)
    for i in range(i_2, len(s2[0])):
        s2_pop.append(i)
    for index in reversed(s1_pop):
        for i in range(loop_range):
            s1[i].pop(index)
    for index in reversed(s2_pop):
        for i in range(loop_range):
            s2[i].pop(index)
    return s1, s2


def getAffinePoint(signal, t):
    i = 0
    while signal[0][i] < t:
        if signal[0][i] == t:
            return signal[1][t]
        i += 1
    if i == 0:
        return signal[1][i] / signal[0][i] * t
    else:
        return (signal[1][i] - signal[1][i - 1]) / (signal[0][i] - signal[0][i - 1]) * (t - signal[0][i - 1]) + signal[1][i - 1]


def getPunctualIntersection(s1, s2):
    i_1 = 0
    i_2 = 0
    start = max(min(s1[0]), min(s2[0]))
    end = min(max(s1[0]), max(s2[0]))

    while i_1 < len(s1[0]) and s1[0][i_1] < start:
        i_1 += 1
    while i_2 < len(s2[0]) and s2[0][i_2] < start:
        i_2 += 1

    temp_1 = [[], [], []]
    temp_2 = [[], [], []]
    while i_1 < len(s1[0]) and i_2 < len(s2[0]) and (s1[0][i_1] <= end or s2[0][i_2] <= end):
        if s1[0][i_1] == s2[0][i_2]:
            temp_1[0].append(s1[0][i_1])
            temp_1[1].append(s1[1][i_1])
            temp_1[2].append(s1[2][i_1])
            temp_2[0].append(s2[0][i_2])
            temp_2[1].append(s2[1][i_2])
            temp_2[2].append(s2[2][i_2])
            i_1 += 1
            i_2 += 1
        elif s1[0][i_1] < s2[0][i_2]:
            temp_2[0].append(s1[0][i_1])
            temp_2[1].append((s2[1][i_2] - s2[1][i_2 - 1]) / (s2[0][i_2] - s2[0][i_2 - 1]) * (s1[0][i_1] - s2[0][i_2 - 1]) + s2[1][i_2 - 1])
            temp_2[2].append(s2[2][i_2 - 1])
            temp_1[0].append(s1[0][i_1])
            temp_1[1].append(s1[1][i_1])
            temp_1[2].append(s1[2][i_1])
            i_1 += 1
        elif s1[0][i_1] > s2[0][i_2]:
            temp_1[0].append(s2[0][i_2])
            temp_1[1].append((s1[1][i_1] - s1[1][i_1 - 1]) / (s1[0][i_1] - s1[0][i_1 - 1]) * (s2[0][i_2] - s1[0][i_1 - 1]) + s1[1][i_1 - 1])
            temp_1[2].append(s1[2][i_1 - 1])
            temp_2[0].append(s2[0][i_2])
            temp_2[1].append(s2[1][i_2])
            temp_2[2].append(s2[2][i_2])
            i_2 += 1
        else:
            raise Exception("Something went wrong in getPunctualIntersection")
    return temp_1, temp_2


def shift(y, v):
    temp = [t - v for t in y[0]]
    i = 0
    while i < len(y[0]) and temp[i] < 0:
        i += 1
    result = [temp[i:], y[1][i:], y[2][i:]]
    return result


def computeAnd(x, y):
    x, y = getPunctualIntersection(x, y)
    values = [min(x[1][i], y[1][i]) for i in range(len(x[0]))]
    derivatives = [min(x[2][i], y[2][i]) for i in range(len(x[0]))]
    return [x[0], values, derivatives]


def computeOr(x, y):
    x, y = getPunctualIntersection(x, y)
    values = [max(x[1][i], y[1][i]) for i in range(len(x[0]))]
    derivatives = [max(x[2][i], y[2][i]) for i in range(len(x[0]))]
    return [x[0], values, derivatives]


def computeEventually(x):
    y_a = shift(x, a)
    y_b = shift(x, b)
    y = computeOr(y_a, y_b)

    s = x[0][0] - b
    t = s
    i = 0
    M = [0]

    z = [[], [], []]

    while t + a < x[0][-1]:
        t = min(x[0][min(M)] - a, x[0][i + 1] - b)
        if t == x[0][min(M)] - a:
            M.remove(min(M))
            s = t
        if t == x[0][i + 1] - b:
            while len(M) != 0 and x[1][x[0].index(x[0][i + 1] - b)] >= x[1][max(M)]:  # x[0][i] - b could be just t
                M.remove(max(M))
            M += [i + 1]
            i += 1
        if s >= x[0][0]:
            z[0].append(s)
            if len(M) > 0:
                z[1].append(computeOr([c[s:t] for c in y], [y[0], [x[1][min(M)]] * len(y[0])])[1 ][0])
            else:
                t_options = [t + a, t + b]
                for t_ in x[0]:
                    if t + a < t_ < t + b:
                        t_options.append(t_)
                    if t_ >= t + b:
                        break
                z[1].append(computeOr([c[s:t + 1] for c in y], [y[0], [max([getAffinePoint(x, t_) for t_ in t_options])] * len(y[0]), y[2]])[1][0])
    return z

if __name__ == '__main__':
    computeEventually(signal)