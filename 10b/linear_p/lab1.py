import pulp
import numpy as np
import matplotlib.pyplot as plt

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

# Add the objective function
problem += x1 + x2

# Add the constraints
problem += 4*x1 + x2 <= 500
problem += x2 <= 300
problem += x1 + x2 <= 150
problem += 4*x1 + x2 <= 300

# Solve the problem
status = problem.solve()

# Print the status and optimal value
print("Status:", pulp.LpStatus[status])
print("Optimal Value:", pulp.value(problem.objective))

# Print the optimal solution
for var in problem.variables():
    print(var.name, "=", var.varValue)

# Define the constraint functions
def constraint1(x):
    return 500 - 4*x

def constraint2(x):
    return np.full_like(x, 300)

def constraint3(x):
    return 150 - x

def constraint4(x):
    return 300 - 4 * x

# Create a grid of x values
x = np.linspace(0, 100, 1000)

# Plot the constraints
plt.plot(x, constraint1(x), label='4*x1 + x2 <= 500')
plt.plot(x, constraint2(x), label='x2 <= 300')
plt.plot(x, constraint3(x), label='x1 + x2 <= 150')
plt.plot(x, constraint4(x), label='4*x1 + x2 <= 300')

# plot the optimal solution
plt.scatter(x1.value(), x2.value(), marker='o', s=100, color='green', label='Optimal solution')

# Shade the feasible region
y5 = np.maximum(constraint1(x), 0)
y6 = np.minimum(constraint4(x), constraint3(x))
plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5, label='Feasible Region')

# Label the plot
plt.title('Feasible Region')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

# Show the plot
plt.show()
