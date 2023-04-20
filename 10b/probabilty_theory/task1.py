import random

# Підкидаємо монету 100 разів та виводимо результат
results = []
for i in range(100):
    result = random.choice(['герб', 'решка'])
    results.append(result)

print(results)

# Обчислюємо ймовірності випадіння герба та решки
num_heads = results.count('герб')
num_tails = results.count('решка')
prob_heads = num_heads / len(results)
prob_tails = num_tails / len(results)

print('Ймовірність випадіння герба: ', prob_heads)
print('Ймовірність випадіння решки: ', prob_tails)
