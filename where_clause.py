# Clearing the screen
import os
os.system('clear')


# Importing sqlite3 module
import sqlite3


# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

	
# Creating a cursor
c = conn.cursor()


# Querying
c.execute("SELECT * FROM customers WHERE last_name = 'Bond'")

items = c.fetchall()

for item in items:
	print(item)

print("********************************************************************************************************************")


c.execute("SELECT * FROM customers WHERE last_name like 'B%' ")

new_query = c.fetchall()

for i in new_query:
	print(i)


# Commiting changes made
conn.commit()

# Closing our connection
conn.close()