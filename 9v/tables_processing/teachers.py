# import openpyxl

# # Replace 'your_file.xlsx' with the actual path to your Excel file
# excel_file_path = 'data_example.xlsx'

# # Load the Excel workbook
# workbook = openpyxl.load_workbook(excel_file_path)

# # Select the active sheet (you can also specify a sheet name)
# sheet = workbook.active

# # Iterate through rows and columns to print cell values
# for row in sheet.iter_rows(values_only=True):
#     print(row)

import pandas as pd

excel_file_path = 'data_example.xlsx'

df = pd.read_excel(excel_file_path, sheet_name="Притула М.І.")

print(df)

print("Sheet Names:", list(df.keys()))

print(df["Unnamed: 2"])

# Drop rows with NaN values
df_cleaned = df.dropna()
# Display the cleaned DataFrame
print("DataFrame after dropping rows with NaN values:")
print(df_cleaned)