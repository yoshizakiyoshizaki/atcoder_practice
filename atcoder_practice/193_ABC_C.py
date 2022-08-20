N = int(input())
num_set = set()
for a in range(2, 10**5 + 1):
    for b in range(2, 1000):
        power = a ** b
        if power <= N:
            num_set.add(power)
            #print("power = ", power)
            #print("a = ", a, "b = ", b)
            #print(num_set)
        else:
            break
print(N - len(num_set))
