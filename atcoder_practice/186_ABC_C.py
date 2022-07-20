# 1回目の商
# print(791 // 8)

# # 最下位
# print(791 % 8)

N = int(input())
count = 0


def judge_ten(x):
    x = str(x)
    if "7" in x:
        return True
    else:
        return False


def judge_eight(x):
    s = ""
    while x > 0:
        s = str(x % 8) + s
        x = x // 8
    if "7" in s:
        return True
    else:
        return False


for num in range(1, N + 1):
    if judge_eight(num) == False and judge_ten(num) == False:
        count += 1

print(count)
