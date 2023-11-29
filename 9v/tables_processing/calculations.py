import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv("sales_data.csv")

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Revenue'], marker='o', color='b', linestyle='-', linewidth=2)

# Adding labels and title
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.title('Monthly Sales Data')

# Display the plot
plt.grid(True)
plt.show()
