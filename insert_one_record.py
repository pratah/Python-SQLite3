# Importing sqlite3 module
import sqlite3

# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

# Creating a cursor
c = conn.cursor()


# Inserting one record at a time
c.execute("INSERT INTO customers VALUES ('John', 'Doe', 'john@email.com')")


# Commiting changes made
conn.commit()

# Closing our connection
conn.close()