import pandas as pd
import mysql.connector

# Extract data from Excel files
top_movies_data = pd.read_excel('Top_movies_dataset.xlsx')
marvel_movies_data = pd.read_excel('marvel_movies_dataset.xlsx')

# Perform JOIN operation
merged_data = pd.merge(top_movies_data, marvel_movies_data, on='year')

# Calculate average worldwide gross by year and category
average_gross_by_year_category = merged_data.groupby(['year', 'category'])['worldwide gross ($m)'].mean()

# Calculate total budget and total worldwide gross by year
total_budget_gross_by_year = merged_data.groupby('year')[['budget  (millions)', 'worldwide gross ($m)']].sum()

# Print the transformed data
print("Average Gross by Year and Category:")
print(average_gross_by_year_category)

print("\nTotal Budget and Gross by Year:")
print(total_budget_gross_by_year)
