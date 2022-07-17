N = int(input())
mountains = []
for num in range(N):
    S, T = map(str, input().split())
    T = int(T)
    mountains.append([T, S])
    mountains.sort(reverse=True)
print(mountains[1][1])
