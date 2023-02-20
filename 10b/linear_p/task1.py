import pulp

# Create a maximization problem
problem = pulp.LpProblem("Maximization Problem", pulp.LpMaximize)

# Define the decision variables
# x = pulp.LpVariable('x', lowBound=0)
# y = pulp.LpVariable('y', lowBound=0)
a = pulp.LpVariable('a', lowBound=0)
b = pulp.LpVariable('b', lowBound=0)
c = pulp.LpVariable('c', lowBound=0)

# Add the objective function
#problem += 2 * x + y
problem += 13 * a + 18 * b + 22 * c

# Add the constraints
# problem += 3 * x + 4 * y <= 25
# problem += 2 * x + y <= 10

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
