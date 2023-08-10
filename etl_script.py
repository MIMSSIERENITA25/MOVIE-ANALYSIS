import pandas as pd
import mysql.connector

# Extract data from Excel files
top_movies_data = pd.read_excel('Top_movies_dataset.xlsx')
marvel_movies_data = pd.read_excel('marvel_movies_dataset.xlsx')
top_movies_data.head()
marvel_movies_data.head()

# Transforming the data
missing_values = top_movies_data.isna().sum()
print(missing_values)
print(top_movies_data.info())      
print(top_movies_data.columns)
print(marvel_movies_data.columns)

# Check for duplicate rows
duplicates = top_movies_data.duplicated()

# Display the duplicate rows
print("Duplicate Rows:")
print(top_movies_data[duplicates])

# Remove duplicate rows
top_movies_data_no_duplicates = top_movies_data.drop_duplicates()

# Display the DataFrame without duplicates
print("\nDataFrame without Duplicates:")
print(top_movies_data_no_duplicates)

# Check for duplicate rows
duplicate = marvel_movies_data.duplicated()

# Display the duplicate rows
print("Duplicate Rows:")
print(marvel_movies_data[duplicate])

# Remove duplicate rows
top_movies_data_no_duplicate = top_movies_data.drop_duplicates()

# Display the DataFrame without duplicates
print("\nDataFrame without Duplicates:")
print(top_movies_data_no_duplicate)

# Convert a column to a specific data type
top_movies_data['year'] = top_movies_data['year'].astype(int)

top_movies_data['year'].head()

# Calculate average worldwide gross by year and category
average_gross_by_year_category = merged_data.groupby(['year', 'category'])['worldwide gross ($m)'].mean()
average_gross_by_year_category.head()

# Join datasets based on common attributes
joined_data = pd.merge(top_movies_data, marvel_movies_data, left_on='title', right_on='film', how='inner')

joined_data.head()


from sklearn.preprocessing import MinMaxScaler

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Normalize 'budget  (millions)' column
top_movies_data['budget  (millions)'] = scaler.fit_transform(top_movies_data[['budget  (millions)']])

top_movies_data['budget  (millions)'] .head()

# Filter movies with a budget greater than a certain value
high_budget_movies = top_movies_data[top_movies_data['budget  (millions)'] > 100]

high_budget_movies.head()

# Check the column names in the DataFrame
print(top_movies_data.columns)

from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Apply label encoding to the 'horror' column
top_movies_data['horror_encoded'] = label_encoder.fit_transform(top_movies_data['horror'])
top_movies_data['horror_encoded'].head()

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Apply Min-Max scaling to the 'budget  (millions)' column
top_movies_data['budget_scaled'] = scaler.fit_transform(top_movies_data[['budget  (millions)']])
top_movies_data['budget_scaled'].head()

top_movies_earnings = top_movies_data['worldwide gross (m)']
top_movies_earnings.head()

marvel_movies_earnings = marvel_movies_data['worldwide gross ($m)']
marvel_movies_earnings.head()

#Loading the data 

import pandas as pd
import sqlalchemy

# Replace these values with your MySQL database connection details
db_username = 'root'
db_password = '#Incorrect05'  # Replace with your actual password
db_host = 'localhost'
db_name = 'movie'  # Replace with your actual database name

# Create a MySQL database connection
db_connection = sqlalchemy.create_engine(f"mysql+mysqlconnector://{db_username}:{db_password}@{db_host}/{db_name}")

# Assuming you have defined your 'top_movies_data' and 'marvel_movies_data'

# Write data to MySQL source tables
top_movies_data.to_sql('source_table1', con=db_connection, if_exists='replace', index=False)
marvel_movies_data.to_sql('source_table2', con=db_connection, if_exists='replace', index=False)

# Join datasets based on movie title
joined_data = pd.merge(top_movies_data, marvel_movies_data, left_on='title', right_on='film', how='inner')

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

# Write transformed data to a new table in the database
average_gross_by_year_category.to_sql('average_gross_by_year_category', con=db_connection, if_exists='replace', index=True, dtype={'category': sqlalchemy.String(length=255)})
total_budget_gross_by_year.to_sql('total_budget_gross_by_year', con=db_connection, if_exists='replace', index=True)

# Close the database connection
db_connection.dispose()

