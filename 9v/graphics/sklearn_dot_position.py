from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# Створення навчальних даних для тривимірної навігації
X_train = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
y_train = np.array([0, 1, 2])

# Ініціалізація та навчання моделі k-найближчих сусідів
model = KNeighborsRegressor(n_neighbors=1)
model.fit(X_train, y_train)

# Тестування моделі на нових даних
X_test = np.array([[1.5, 1.5, 1.5]])
predicted_location = model.predict(X_test)
print("Передбачене місцезнаходження:", predicted_location)
