def fibonacci_ser(m):
    if(m <= 1):
        return m
    else:
        return(fibonacci_ser(m-1) + fibonacci_ser(m-2))


m = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(m):
    print(fibonacci_ser(i))

