import csv

# Data to be written to the CSV file
data = [
    ['Month', 'Revenue'],
    ['Jan', 1000],
    ['Feb', 1200],
    ['Mar', 800],
    ['Apr', 1500],
    ['May', 1300],
    ['Jun', 1600],
    ['Jul', 900],
    ['Aug', 1100],
    ['Sep', 1400],
    ['Oct', 1200],
    ['Nov', 1000],
    ['Dec', 1800]
]

# Specify the file name
csv_file = 'sales_data.csv'

# Writing data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")
