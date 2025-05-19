import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\SuperMarket Analysis.csv")

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])

# Create 'Month' column
df['Month'] = df['Date'].dt.month_name()
print(df['Month'])

print("-------------------------------------------------")
# Check for duplicates
print(df.duplicated().sum())

#save clean data
df.to_csv("cleaned_sales_data.csv", index=False)
