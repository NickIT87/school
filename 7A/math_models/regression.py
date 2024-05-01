# Імпорт бібліотек
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Згенерувати випадкові дані
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Площа будинків
y = 5 + 3 * X + np.random.randn(100, 1)  # Ціна будинків

# Побудова моделі лінійної регресії
model = LinearRegression()
model.fit(X, y)

# Відображення даних та побудованої лінії регресії
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Лінійна регресія')
plt.xlabel('Площа будинку (квадратні фути)')
plt.ylabel('Ціна будинку (тисячі доларів)')
plt.show()

# Вивід коефіцієнтів моделі
print("Коефіцієнт навчання:", model.coef_)
print("Вільний член:", model.intercept_)
