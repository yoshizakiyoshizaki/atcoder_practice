X, K, D = list(map(int, input().split()))

X = abs(X)

if X - K*D > 0:
    print(abs(X - K*D))
else:
    move_count = K - X//D
    before_jump = X - D*(X//D)
    after_jump = before_jump - D

    if move_count % 2 == 0:
        print(abs(before_jump))
    else:
        print(abs(after_jump))
