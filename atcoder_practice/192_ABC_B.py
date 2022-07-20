
N, K = map(int, input().split())


def g1(N):
    x = str(N)
    x = list(x)
    # x.remove("0")
    x.sort(reverse=True)
    x = "".join(x)
    return int(x)


def g2(N):
    y = str(N)
    y = list(y)
   # y.remove("0")
    y.sort()
    y = "".join(y)
    return int(y)


def f(N):
    return g1(N) - g2(N)


a0 = N
for num in range(K):
    a0 = f(a0)

print(a)
