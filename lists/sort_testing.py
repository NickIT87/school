from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timeit
def bubble_sort(m):
    trigger = True
    while trigger:
        trigger = False
        for i in range(len(m)-1):
            if m[i] > m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]
                trigger = True


@timeit
def select_sort(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]


m = [34, 23, 45, 27, 17, 56, 52]
bubble_sort(m)

n = [34, 23, 45, 27, 17, 56, 52]
select_sort(n)