N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []

for num in range(N):
    if A[num] != X:
        ans.append(A[num])

print(*ans)
