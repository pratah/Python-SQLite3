# Importing sqlite3 module
import sqlite3

# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

# Creating a cursor
c = conn.cursor()


# Inserting multiple rows
customers = [
				('Jason', 'Bourne', 'jason@email.com'), 
				('James', 'Bond', 'james@email'), 
				('Red', 'Sparrow', 'red@email'), 
				('Nathan', 'Muir', 'nathan@email.com')
			]

c.executemany("INSERT INTO customers VALUES (?,?,?)", customers)


# Commiting changes made
conn.commit()

# Closing our connection
conn.close()