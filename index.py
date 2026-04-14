python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming it is in CSV format)
df = pd.read_csv('uae_real_estate_market_data.csv')

# Example: Calculate average property price by city
average_prices_by_city = df.groupby('City')['Property Price'].mean()

# Plot the average property prices
plt.figure(figsize=(10, 6))
average_prices_by_city.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Average Property Prices by City in UAE')
plt.xlabel('City')
plt.ylabel('Average Property Price (AED)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Example: Filter properties with high rental yields
high_yield_properties = df[df['Rental Yield'] > 7.0]
print(high_yield_properties[['Property Name', 'City', 'Rental Yield']])

# Save high-yield properties to a new CSV
high_yield_properties.to_csv('high_yield_properties.csv', index=False)
