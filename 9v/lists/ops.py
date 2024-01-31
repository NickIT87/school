array = [1, 2, 3, 4, 5]
sum_values = sum(array)
print(f"Сума значень елементів: {sum_values}")

array = [1, 2, 3, 4, 5]
condition = lambda x: x % 2 == 0  # Приклад: вибираємо парні елементи
sum_filtered_values = sum(filter(condition, array))
print(f"Сума елементів, які задовольняють умову: {sum_filtered_values}")

array = [1, 2, 3, 4, 5]
condition = lambda x: x % 2 == 0  # Приклад: вибираємо парні елементи
count_filtered_values = sum(1 for x in array if condition(x))
print(f"Кількість елементів, які задовольняють умову: {count_filtered_values}")

# Example 1: Squaring each element in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]

# Example 2: Converting temperatures from Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(fahrenheit_temps)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]

from functools import reduce

# Example 1: Finding the product of all elements in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# Output: 120

# Example 2: Concatenating strings in a list
words = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, words)
print(concatenated_string)
# Output: Hello World!

