import sqlite3
# Create a connection to database
conn = sqlite3.connect('northwind_small.sqlite3')
# Create a cursor object
cur = conn.cursor()

# Query to find the ten most expensive items (per unit price) in the database
expensive_items = cur.execute("SELECT * FROM Product ORDER BY UnitPrice\
     DESC LIMIT 10;")
print(expensive_items.fetchall())

# Query to calculate the average age of an employee at time of hiring
avg_hire_age = cur.execute("SELECT ROUND (avg(HireDate - BirthDate), 2)\
    FROM Employee;")
print(f"Employee's average age at time of hiring is:\
    {avg_hire_age.fetchone()[0]}")

# (*Stretch*) Query to calculate how the average age of employee at hire 
# varies by city
avg_age_by_city = cur.execute("SELECT City, avg(HireDate - BirthDate) \
    FROM Employee GROUP BY City;")
print(avg_age_by_city.fetchall())

"""
Query to find the ten most expensive items (per unit price) in the database
and their suppliers.
"""
ten_most_expensive = cur.execute("SELECT prod.*, supp.CompanyName \
    FROM Product AS prod INNER JOIN Supplier AS supp \
    ON supp.Id = prod.SupplierId ORDER BY UnitPrice DESC LIMIT 10;")
print(ten_most_expensive.fetchall())

# Query to find the the largest category (by number of unique products in it)
largest_category = cur.execute("SELECT cat.CategoryName, \
    count(DISTINCT ProductName) FROM Product AS prod \
    INNER JOIN Category as cat ON cat.Id = prod.CategoryId \
    WHERE prod.Discontinued=0 GROUP BY CategoryId \
    ORDER BY count(DISTINCT ProductName) DESC LIMIT 1;")
print(f'The largest category (by number of unique products in it) is \
    {largest_category.fetchone()[0]}')
""" 
This query can also be accomplished without JOINs by utilizing the 
ProductDetails_V table as follows:
cur.execute("SELECT CategoryName, count(DISTINCT ProductName) \
    FROM ProductDetails_V WHERE Discontinued=0 GROUP BY CategoryId\
    ORDER BY count(DISTINCT ProductName) DESC LIMIT 1;")
I completed the query with JOINs because it was in Part 3 of the markdown file
"""

# (*Stretch*) Query to find the employee with the most territories 
most_territories = cur.execute("SELECT emp.*, count(DISTINCT TerritoryId)\
    FROM Employee AS emp INNER JOIN EmployeeTerritory as empt \
    ON emp.Id = empt.EmployeeId GROUP BY EmployeeId \
    ORDER BY count(DISTINCT TerritoryId) DESC LIMIT 1;")
print(f'The employee with the most territories is:\
    {most_territories.fetchone()}')

# Close cursor and connection objects
cur.close()
conn.close()