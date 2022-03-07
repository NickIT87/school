def cnt_sum(a):
    cnt = len(str(a))      
    ansv = []

    while cnt:
        cnt -= 1
        x = a // 10
        y = a % 10
        a = x
        ansv.append(y)

    return sum(ansv)


# точка входа
if __name__ == "__main__":
    print(cnt_sum(253111))