import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define two coplanar vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Create a figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the origin
ax.scatter(0, 0, 0, color='red', marker='o', label='Origin')

# Plot the vectors
ax.quiver(0, 0, 0, vector1[0], vector1[1], vector1[2], color='blue', label='Vector 1')
ax.quiver(0, 0, 0, vector2[0], vector2[1], vector2[2], color='green', label='Vector 2')

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set axis limits
ax.set_xlim([0, max(vector1[0], vector2[0]) + 1])
ax.set_ylim([0, max(vector1[1], vector2[1]) + 1])
ax.set_zlim([0, max(vector1[2], vector2[2]) + 1])

# Set the title
plt.title('Coplanar Vectors in 3D Space')

# Add legend
ax.legend()

# Show the plot
plt.show()
