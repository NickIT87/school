import matplotlib.pyplot as plt

# Create a figure object
fig = plt.figure()

# Add a subplot
ax = fig.add_subplot(111)

# Plot some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y)

# Set the axis labels
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')

# Save the figure as a PDF file
fig.savefig('output.pdf', bbox_inches='tight')
