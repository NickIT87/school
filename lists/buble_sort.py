m = [34, 23, 45, 27, 17, 56, 52]
print(m)


def bubble_sort(m):
    trigger = True
    while trigger:
        trigger = False
        for i in range(len(m)-1):
            if m[i] > m[i+1]:
                m[i], m[i+1] = m[i+1], m[i]
                trigger = True
        

bubble_sort(m)        
print(m)