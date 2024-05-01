import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Завантажимо набір даних про іриси
iris = load_iris()
X = iris.data
y = iris.target

# Розділимо дані на тренувальні та тестувальні
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Використовуємо k-NN для класифікації
k = 5
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Зробимо передбачення на тестових даних
y_pred = knn.predict(X_test)

# Оцінимо точність класифікації
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Побудуємо графік для відображення реальних та передбачених значень
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Actual Labels')

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Predicted Labels')

plt.tight_layout()
plt.show()
