import pandas as pd
import numpy as np
 
df = pd.read_csv("AQI_Data.csv")
 
print("First 8 rows:")
print(df.head(8))
 
print("\nLast 5 rows:")
print(df.tail(5))
 
print("\nData types:")
print(df.dtypes)
 
print("\nCount of non-null values:")
print(df.count())
 
grouped = df.groupby('City')
 
mean_aqi = grouped['AQI'].apply(np.mean)
max_pm25 = grouped['PM2.5'].apply(np.max)
min_pm10 = grouped['PM10'].apply(np.min)
 
stats = pd.DataFrame({
    'Mean AQI': mean_aqi,
  
    'Max PM2.5': max_pm25,
  
    'Min PM10': min_pm10
})
 
print("\nStatistics for each city:")
print(stats)

stats_sorted = stats.sort_values(by='Mean AQI', ascending=False)
 
print("\nStatistics for each city sorted by Mean AQI (descending):")
print(stats_sorted)

output_file = "Sorted_AQI_Data.csv"
stats_sorted.to_csv(output_file, index=True)

 

