# Clearing the screen
import os
os.system('clear')


# Importing sqlite3 module
import sqlite3


# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

	
# Creating a cursor
c = conn.cursor()


# Updating Records
c.execute(""" UPDATE customers SET first_name = "Marty"
			WHERE last_name = "Doe"
		""")


# Commiting changes made
conn.commit()


# Querying
c.execute("SELECT * FROM customers")

items = c.fetchall()

for item in items:
	print(item)


# Closing our connection
conn.close()