import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 200, 1000)

x2_1 = 500 - 4 * x1
x2_2 = 300 - 4 * x1
x2_3 = 150 - x1

plt.plot(x1, x2_1, label='4x1 + x2 <= 500')
plt.plot(x1, x2_2, label='4x1 + x2 <= 300')
plt.plot(x1, x2_3, label='x1 + x2 <= 150')
plt.axhline(y=300, color='g', label='x2 <= 300')

plt.xlim((0, 200))
plt.ylim((0, 350))
plt.xlabel('x1')
plt.ylabel('x2')

# Заливка допустимої області
plt.fill_between(x1, np.minimum(x2_1, x2_2), x2_3, where=(x1 <= 100), color='gray', alpha=0.3)

# Відзначення точок B, C, D
plt.plot(100, 50, 'ro', label='B (100, 50)')
plt.plot(50, 100, 'bo', label='C (50, 100)')
plt.plot(60, 60, 'go', label='D (60, 60)')

plt.legend()
plt.grid(True)
plt.show()
