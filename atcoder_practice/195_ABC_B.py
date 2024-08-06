A, B, W = map(int, input().split())
# A以上B以下で変化する
ans = []
for a in range(A, B + 1):
    for b in range(A, B + 1):
        for x in range(10001):
            for y in range(1001):
                if a * x + b * y == W * 1000:
                    ans.append()
                else:
                    pass
if len(ans) != 0:
    print(ans)
else:
    print("UNSATISFIABLE")
