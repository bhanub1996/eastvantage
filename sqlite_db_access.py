import sqlite3

# Connecting to the SQLite3 database
conn = sqlite3.connect(r"C:\Users\bhanu\eastvantage.db")
cursor = conn.cursor()

# SQL query to get total quantities of each item bought/customer aged 18-35
query = """
    SELECT c.customer_id, i.item_name, COALESCE(SUM(o.quantity), 0) AS total_quantity
    FROM Customer c
    JOIN Sales s ON c.customer_id = s.customer_id
    JOIN Orders o ON s.sales_id = o.sales_id
    JOIN Items i ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35
    GROUP BY c.customer_id, i.item_name
    HAVING total_quantity > 0
"""

# Execute the query written above
cursor.execute(query)

# Fetching the query results
results = cursor.fetchall()

for row in results:
    customer_id, item_name, total_quantity = row
    print(f"Customer {customer_id}: {item_name} - {total_quantity} items")

# Finally Closing the connection
conn.close()
