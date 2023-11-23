# Основні етапи швидкого сортування:

# 1. Вибір опорного елемента: Вибрати елемент з масиву як опорний.
# 2. Розділення масиву: Розмістіть елементи так, щоб елементи менше
#    опорного були ліворуч від нього, а більше - праворуч.
# 3. Рекурсивне сортування: Рекурсивно сортувати ліву і праву частини масиву.
# 4. Об'єднання: Об'єднати відсортовані ліву частину, опорний елемент і
#    відсортовану праву частину.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example usage:
my_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(my_list)
print(sorted_list)
