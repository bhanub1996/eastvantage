import pandas as pd
import sqlite3

# Connect to the SQLite3 database
conn = sqlite3.connect(r"C:\Users\bhanu\eastvantage.db")

# Read tables into pandas DataFrames
customers_df = pd.read_sql_query("SELECT * FROM Customer WHERE age BETWEEN 18 AND 35", conn)
sales_df = pd.read_sql_query("SELECT * FROM Sales", conn)
items_df = pd.read_sql_query("SELECT * FROM Items", conn)
orders_df = pd.read_sql_query("SELECT * FROM Orders", conn)

# Merge DataFrames to get required information
merged_df = pd.merge(customers_df, sales_df, on='customer_id')
merged_df = pd.merge(merged_df, orders_df, on='sales_id')
merged_df = pd.merge(merged_df, items_df, on='item_id')

# Group by customer_id and item_name and sum quantities
grouped_df = merged_df.groupby(['customer_id', 'item_name'])['quantity'].sum().reset_index()

# Filter out items with total quantity = 0
filtered_df = grouped_df[grouped_df['quantity'] > 0]

# Display the result
print(filtered_df)

# Close the connection
conn.close()
