def solve(number):
    digit1 = number // 100
    number = number - digit1 * 100
    digit2 = number // 10
    digit3 = number - digit2 * 10
    sum = digit1 + digit2 + digit3
    print(sum)
