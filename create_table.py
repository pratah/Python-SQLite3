# Importing sqlite3 module
import sqlite3

# Establishing a connection and create DB
conn = sqlite3.connect('customer.db')

# Creating a cursor
c = conn.cursor()