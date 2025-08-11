import pandas as pd
import matplotlib.pyplot as plt

# 1. Create a sample CSV (this is for testing; replace with your actual CSV later)
data = {
    'Product': ['A', 'B', 'A', 'C','D','B', 'C', 'D'],
    'Sales':   [200, 450, 300, 700, 150, 400, 250,350],
    'Quantity':[3, 6, 5, 8, 2, 4, 3,5]
}
df_sample = pd.DataFrame(data)
df_sample.to_csv('sales.csv', index=False)

# 2. Load CSV using Pandas
df = pd.read_csv('sales.csv')
print("First 5 rows of the dataset:\n", df.head())

# 3. Dataset information
print("\nDataset Info:")
print(df.info())

print("\nDataset Shape (rows, columns):", df.shape)

# 4. Group by 'Product' and sum Sales
sales_by_product = df.groupby('Product')['Sales'].sum().reset_index()
print("\nTotal Sales by Product:\n", sales_by_product)

# 5. Visualization: Bar chart of Sales by Product
plt.figure(figsize=(8, 5))
plt.bar(sales_by_product['Product'], sales_by_product['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 6. Filter rows: Sales greater than 500
high_sales = df[df['Sales'] > 500]
print("\nRows where Sales > 500:\n", high_sales)

# 7. Check for missing values
print("\nMissing values in dataset:\n", df.isnull().sum())