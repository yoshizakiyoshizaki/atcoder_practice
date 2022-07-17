N = int(input())
A =list(map(int, input().split()))
B = list(map(int, input().split()))
product = 0
for num in range(N):
    product += A[num] * B[num]

if product == 0:
    print("Yes")
else:
    print("No")
    