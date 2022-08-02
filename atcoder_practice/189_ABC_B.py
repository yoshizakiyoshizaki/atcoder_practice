N, X = map(int, input().split())
sum_alcohol = 0

for num in range(1, N + 1):

    V, P = map(int, input().split())
    alcohol = V * P
    #alcohol = round(V * P/100)
    sum_alcohol += alcohol
    if sum_alcohol > X * 100:
        print(num)
        exit()

# if sum_alcohol <= X:
print(-1)
