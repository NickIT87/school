import pulp
import numpy as np
import matplotlib.pyplot as plt

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
a = pulp.LpVariable('a', lowBound=0)
b = pulp.LpVariable('b', lowBound=0)
c = pulp.LpVariable('c', lowBound=0)

# Add the objective function
problem += 13 * a + 18 * b + 22 * c

# Add the constraints
problem += a + b + c == 300
problem += a >= 50
problem += b >= 40
problem += c <= 40

# Solve the problem
status = problem.solve()

# Print the status and optimal value
print("Status:", pulp.LpStatus[status])
print("Optimal Value:", pulp.value(problem.objective))

# Print the optimal solution
for var in problem.variables():
    print(var.name, "=", var.varValue)

a_value = a.value()
b_value = b.value()
c_value = c.value()
z_value = problem.objective.value()

# plot the feasible region
a_vals = np.linspace(0, 300, 100)
b_vals1 = 300 - a_vals
b_vals2 = 40 * np.ones_like(a_vals)
c_vals = np.linspace(0, 40, 100)
plt.plot(a_vals, b_vals1, 'r-', label='a + b + c = 300')
plt.plot(a_vals, b_vals2, 'b-', label='c <= 40')
plt.plot(50 * np.ones_like(c_vals), c_vals, 'g-', label='a >= 50')

# plot the optimal solution
plt.plot(a_value, b_value, 'go', markersize=10, label='Optimal solution')

# add labels and legend
plt.xlabel('a')
plt.ylabel('b')
plt.legend()

# show the plot
plt.show()