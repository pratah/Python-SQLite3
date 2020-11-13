# Clearing the screen
import os
os.system('clear')


# Importing sqlite3 module
import sqlite3


# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

	
# Creating a cursor
c = conn.cursor()


# Drop table
c.execute("DROP TABLE customers")

# Commiting changes made
conn.commit()

c.execute("SELECT rowid, * FROM customers LIMIT 2 ")

items = c.fetchall()

for item in items:
	print(item)


# Closing our connection
conn.close()