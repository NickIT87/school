import pulp
import numpy as np
import matplotlib.pyplot as plt

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)

# Add the objective function
problem += 4 * x1 + x2

# Add the constraints
problem += 6*x1 + x2 <= 430
problem += 3*x2 <= 250
problem += x1 + 4*x2 <= 200
problem += 6*x1 + x2 <= 600

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
    return -6*x + 430

def constraint2(x):
    return np.full_like(x, 83.33)

def constraint3(x):
    return -0.25*x + 50

def constraint4(x):
    return -6*x + 600

# Create a grid of x values
x = np.linspace(0, 100, 1000)

# Plot the constraints
plt.plot(x, constraint1(x), label='6*x1 + x2 <= 430')
plt.plot(x, constraint2(x), label='3*x2 <= 250')
plt.plot(x, constraint3(x), label='x1 + 4*x2 <= 200')
plt.plot(x, constraint4(x), label='6*x1 + x2 <= 600')

# plot the optimal solution
plt.scatter(x1.value(), x2.value(), marker='o', s=100, color='green', label='Optimal solution')

# Label the plot
plt.title('Feasible Region')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()

# Show the plot
plt.show()
