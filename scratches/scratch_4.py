a = 2
b = 4

ts = [0, 5, 6, 7, 8]
y = [0, 0, -1, -1, 0]
dy = [0.0, -1.0, 0.0, 1.0, 0]

s = ts[0] - b
t = s
i = 0
M = {ts[0]}


def ysignal(t):
    before = 0
    for i in range(len(ts)):
        if ts[i] > t:
            break
        else:
            before = i
    assert(before < len(ts))
    return dy[i] * (t - ts[i])


while t + a < ts[-1]:
    print(f"s = {s}, t = {t}, i = {i}, M = {M}")
    print(f"ts[min(M)] - a = {min(M) - a}")
    if i + 1 < len(ts):
        print(f"ts[i + 1] - b = {ts[i + 1] - b}")
        t = min(min(M) - a, ts[i + 1] - b)
    else:
        print("Ran out of samples, only the first case can happen now")
        t = min(M) - a
    print(f"t = {t}")
    if t == min(M) - a:
        M.remove(min(M))
        s = t
    if i + 1 < len(ts) and t == ts[i + 1] - b:
        while len(M) > 0 and ysignal(ts[i + 1] - b) >= ysignal(max(M)):
            M.remove(max(M))
        M.add(ts[i + 1])
        if i + 1 < len(ts):
            i += 1
    elif i + 1 < len(ts) and len(M) == 0:
        if dy[i] > 0:
            M.add(t + b)
        else:
            M.add(t + a + 1)
    if s >= ts[0]:
        print(f"z|[s,t) = [{s},{t})")
