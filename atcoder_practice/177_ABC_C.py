N = int(input())
A = list(map(int, input().split()))
A_sum = sum(A)
mod = 10**9+7
ans = 0
for num in range(N):
    A_sum = A_sum - A[num]
    ans += A[num] * A_sum
ans %= mod
print(ans)
