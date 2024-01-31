import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vector components
x = 2
y = 3
z = 1

# Create a 3D figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vector using quiver
ax.quiver(0, 0, 0, x, y, z, color='b')

# Set the aspect ratio of the plot to be equal
ax.set_box_aspect([1, 1, 1])

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Vector Plot')

# Show the plot
plt.show()
