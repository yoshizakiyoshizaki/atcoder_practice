A, B = map(int, input().split())


def lcm_r(a, b):
    remainder = a % b
    if remainder == 0:
        return a
    #print("ans", a * lcm_r(b, remainder) / remainder)

    return a * lcm_r(b, remainder) / remainder


print(round(lcm_r(A, B)))
