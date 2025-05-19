import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Hp\OneDrive\Desktop\SuperMarket Analysis.csv")

#eda
#sales over time
sales_by_date = df.groupby('Date')['Sales'].sum()
plt.figure(figsize=(12, 5))
sales_by_date.plot()
plt.title('Total Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

#sales over city
plt.figure(figsize=(8, 5))
sns.barplot(x='City', y='Sales', data=df, estimator=sum)
plt.title('Total Sales by City')
plt.show()

#sales by product line

plt.figure(figsize=(10, 6))
sns.barplot(x='Product line', y='Sales', data=df, estimator=sum)
plt.title('Sales by Product Line')
plt.xticks(rotation=45)
plt.show()

#payment details
sns.countplot(data=df, x='Payment')
plt.title("Payment Method Distribution")
plt.show()

#gender vs sales
sns.barplot(x='Gender', y='Sales', data=df, estimator=sum)
plt.title("Sales by Gender")
plt.show()

#correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


