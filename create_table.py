# Importing sqlite3 module
import sqlite3

# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

# Creating a cursor
c = conn.cursor()

# Create a table
c.execute(""" CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")

# Commiting changes made
conn.commit()

# Closing our connection
conn.close()