# приклад підручника
# def return_value(delivery_amounts):
#     F = [0] * (delivery_amounts + 1)
#     F[0] = 1; F[1] = 1; F[2] = 2; F[3] = 3; F[4] = 5
#     for i in range(5, delivery_amounts+1):
#         F[i] = F[i-1]+F[i-2]+F[i-5]
#     return F
# print(return_value(13))

# приклад з інтернета
def count_ways_to_make_change(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1  # Тільки один спосіб представити решту (нічого не робити)

    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]

    return ways[amount]


def return_change(amount, coins):
    coins.sort(reverse=True)  # Сортування монет за зменьшенням номіналу
    change = []
    
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
    
    return change

# Приклад використання
amount_to_make = 10
available_coins = [1, 5, 10, 25]
available_coins2 = [25, 10, 5, 1]

result = count_ways_to_make_change(amount_to_make, available_coins)
print(f"Кількість способів представити {amount_to_make} центів: {result}")

change_result = return_change(amount_to_make, available_coins)
print(f"Решта: {change_result}")

change_result2 = return_change(amount_to_make, available_coins2)
print(f"Решта: {change_result2}")