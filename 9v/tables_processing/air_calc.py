import matplotlib.pyplot as plt


x = ['azot', 'oxygen', 'gas', 'dioksyd']
y = [78.08, 20.94, 0.94, 0.04]

fig, ax = plt.subplots()
ax.pie(y, labels=x, autopct='%1.2f%%')

plt.show()
