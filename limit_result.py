# Clearing the screen
import os
os.system('clear')


# Importing sqlite3 module
import sqlite3


# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

	
# Creating a cursor
c = conn.cursor()


# Query using AND OR
c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%@email' AND first_name LIKE 'Ja%' ")

items = c.fetchall()

for item in items:
	print(item)


# Commiting changes made
conn.commit()

# Closing our connection
conn.close()