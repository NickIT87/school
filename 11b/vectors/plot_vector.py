import matplotlib.pyplot as plt

# Define the vector components
x = 2
y = 3

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the vector using quiver
ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='b')

# Set the aspect ratio of the plot to be equal
ax.set_aspect('equal')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Vector Plot')

# Show the plot
plt.grid(True)
plt.show()
