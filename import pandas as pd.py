import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('unemployment_data.csv')

# Data Overview
print("Data Head:\n", data.head())
print("\nData Info:\n", data.info())
print("\nData Description:\n", data.describe())

# Data Cleaning
data.dropna(inplace=True)  # Drop rows with missing values

# Data Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Unemployment_Rate', data=data, marker='o')
plt.title('Unemployment Rate in India Over Years')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Year', y='Urban_Unemployment', data=data, marker='o', label='Urban')
sns.lineplot(x='Year', y='Rural_Unemployment', data=data, marker='o', label='Rural')
plt.title('Urban vs Rural Unemployment Rate in India')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.show()

# Basic Analysis
avg_unemployment = data['Unemployment_Rate'].mean()
max_unemployment = data['Unemployment_Rate'].max()
min_unemployment = data['Unemployment_Rate'].min()

print(f'Average Unemployment Rate: {avg_unemployment:.2f}%')
print(f'Maximum Unemployment Rate: {max_unemployment:.2f}%')
print(f'Minimum Unemployment Rate: {min_unemployment:.2f}%')
