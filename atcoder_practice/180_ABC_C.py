N = int(input())

# for num in range(N, 0, -1):

#     if N % num == 0:
#         print(N // num)
num_list = []
num = 1
while num**2 <= N:
    # print(num)
    if N % num == 0:
        # print(num)
        num_list.append(num)
        if num != N // num:
            #print(N // num)
            num_list.append(N // num)
    num += 1

num_list.sort()
for i in num_list:
    print(i)
