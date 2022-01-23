# arithmetic progression 
def s(n):
    for j in range(n+1):
        print('iterator: {0}, value: {1}'.format(j, ((j + 1)/2)*j))
    print('final value: {}'.format(((n + 1)/2)*n))

s(100)

