import sqlite3
# Create a connection to database
conn = sqlite3.connect('demo_data.sqlite3')
# Create a cursor object
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS demo (s varchar(1), \
    x int, y int); ")

# Insert data in demo table
cur.execute("INSERT INTO demo (s, x, y) VALUES ('g', 3, 9);")
cur.execute("INSERT INTO demo (s, x, y) VALUES ('v', 5, 7);")
cur.execute("INSERT INTO demo (s, x, y) VALUES ('f', 8, 7);")

conn.commit()

"""
Query to count how many rows are in the demo table. 
Output: The number of rows in the demo table is:    3
"""
row_count = cur.execute("SELECT count(*) FROM demo;")
print(f'The number of rows in the demo table is:\
    {row_count.fetchone()[0]}')

"""
Query to find how many rows are there where both `x` and `y` are at least 5
The number of rows in the demo table where both 'x' and 'y' are at least 5 is: 2
"""
xy_at_least_5 = cur.execute("SELECT count(*) FROM demo \
                            WHERE x >= 5 AND y >= 5;")
print(f"The number of rows in the demo table where both 'x' and 'y'\
    are at least 5 is: {xy_at_least_5.fetchone()[0]}")

"""
Query to find how many unique values of `y` there are in the demo table
The number of unique 'y' values in the demo table is:  2
"""
unique_y = cur.execute("SELECT COUNT (DISTINCT y) FROM demo;")
print(f"The number of unique 'y' values in the demo table is:\
    {unique_y.fetchone()[0]}")

# Close cursor and connection objects
cur.close()
conn.close()