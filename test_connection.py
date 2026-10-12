
import mysql.connector
import csv

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sales_management_system"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT name, product_name, gross_sales,
           received_amount, pending_amount
    FROM customer_sales
    ORDER BY pending_amount DESC
""")

rows = cursor.fetchall()

with open("customer_sales_report.csv", "w",
          newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Customer Name", "Product", "Gross Sales",
        "Received Amount", "Pending Amount"
    ])
    writer.writerows(rows)

cursor.close()
conn.close()

print("Customer sales report exported successfully!")
print("File: customer_sales_report.csv")
