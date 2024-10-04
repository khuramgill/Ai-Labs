import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
weather_data = pd.read_csv('weather_data.csv')

# NumPy Task - Convert Temperature column to NumPy array and calculate stats
temperature_array = weather_data['Temperature'].to_numpy()
mean_temp = np.mean(temperature_array)
median_temp = np.median(temperature_array)
std_temp = np.std(temperature_array)

# Pandas Task - Filter days with Temperature > 30°C and Weather Condition = 'Sunny'
sunny_hot_days = weather_data[(weather_data['Temperature'] > 30) & (weather_data['Weather Condition'] == 'Sunny')]
num_sunny_hot_days = sunny_hot_days.shape[0]

# Pandas Task - Group by Weather Condition and calculate average Humidity
avg_humidity_by_condition = weather_data.groupby('Weather Condition')['Humidity'].mean()

# Matplotlib Task - Plot temperature variation over the year
plt.figure(figsize=(10, 6))
plt.plot(weather_data['Date'], weather_data['Temperature'], color='orange', label='Temperature')
plt.title('Temperature Variation Over the Year')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.legend()
plt.show()

# Matplotlib Task - Bar plot of number of days for each weather condition
weather_counts = weather_data['Weather Condition'].value_counts()
plt.figure(figsize=(6, 4))
weather_counts.plot(kind='bar', color=['yellow', 'blue', 'gray'])
plt.title('Number of Days for Each Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Days')
plt.show()

mean_temp, median_temp, std_temp, num_sunny_hot_days, avg_humidity_by_condition
