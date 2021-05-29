def reversed(x: int) -> int:
    temp = 0
    div = 0
    if x <= -2 ** 31 or x >= 2 ** 31 - 1:
        return 0
    elif x == 0:
        return 0
    else:
        flag = 0
        if x > 0:
            flag = 1
        x = abs(x)
        while 1:
            div = x % 10
            temp = temp * 10 + div
            if x >= 10:
                x = int(x / 10)
                continue
            else:
                if temp <= -2 ** 31 or temp >= 2 ** 31 - 1:
                    return 0
                if flag == 0:
                    return -temp
                else:
                    return temp


if __name__ == '__main__':
    x = 1534236469
    print(reversed(x))
