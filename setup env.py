# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\SuperMarket Analysis.csv")

# Display first few rows
print(df.head())

print("-------------------------------------------------------------------------------")
# Basic info
df.info()

print("---------------------------------------------------------------------")
# Check null values
print(df.isnull().sum())

print("-----------------------------------------------------------------")
# Basic stats
print(df.describe(include='all'))


