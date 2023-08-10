# Calculate summary statistics for top movies
top_mean = top_movies_data['worldwide gross (m)'].mean()
top_median = top_movies_data['worldwide gross (m)'].median()
top_min = top_movies_data['worldwide gross (m)'].min()
top_max = top_movies_data['worldwide gross (m)'].max()
top_std = top_movies_data['worldwide gross (m)'].std()

# Calculate summary statistics for Marvel movies
marvel_mean = marvel_movies_data['worldwide gross ($m)'].mean()
marvel_median = marvel_movies_data['worldwide gross ($m)'].median()
marvel_min = marvel_movies_data['worldwide gross ($m)'].min()
marvel_max = marvel_movies_data['worldwide gross ($m)'].max()
marvel_std = marvel_movies_data['worldwide gross ($m)'].std()

# Print summary statistics
print("Summary Statistics for Top Movies:")
print(f"Mean: {top_mean:.2f}")
print(f"Median: {top_median:.2f}")
print(f"Minimum: {top_min:.2f}")
print(f"Maximum: {top_max:.2f}")
print(f"Standard Deviation: {top_std:.2f}")

print("\nSummary Statistics for Marvel Movies:")
print(f"Mean: {marvel_mean:.2f}")
print(f"Median: {marvel_median:.2f}")
print(f"Minimum: {marvel_min:.2f}")
print(f"Maximum: {marvel_max:.2f}")
print(f"Standard Deviation: {marvel_std:.2f}")

import matplotlib.pyplot as plt

# Plot histogram for top movies
plt.hist(top_movies_data['worldwide gross (m)'], bins=20, alpha=0.5, label='Top Movies')
# Plot histogram for Marvel movies
plt.hist(marvel_movies_data['worldwide gross ($m)'], bins=20, alpha=0.5, label='Marvel Movies')

plt.xlabel('Worldwide Gross Earnings ($m)')
plt.ylabel('Frequency')
plt.title('Comparison of Worldwide Gross Earnings')
plt.legend()
plt.show()

# Calculate average worldwide gross earnings for each category in top movies dataset
average_gross_top_movies = top_movies_data.groupby('horror')['worldwide gross (m)'].mean()

# Calculate average worldwide gross earnings for each category in Marvel movies dataset
average_gross_marvel_movies = marvel_movies_data.groupby('category')['worldwide gross ($m)'].mean()

# Display the average worldwide gross earnings for each category
print("Average Worldwide Gross Earnings for Top Movies:")
print(average_gross_top_movies)

print("\nAverage Worldwide Gross Earnings for Marvel Movies:")
print(average_gross_marvel_movies)

#Results from the analysis

#Marvel movies, on average, tend to earn more worldwide gross than the top movies, as evidenced by the higher mean and median values.
#The standard deviation for both datasets suggests that there is a considerable variation in the earnings of movies, indicating that there are both high-performing and low-performing movies in each dataset.
#The wide range between the minimum and maximum values for both datasets suggests a diverse distribution of earnings.
#Marvel movies have a wider spread of earnings, as indicated by the higher standard deviation, suggesting a higher variability in their financial performance compared to the top movies.


