# :arrow_right: Querying data with python :arrow_left:

---

## Establishing a connection in memory
`conn = sqlite3.connect(':memory:')` <br><br>
:warning: Changes made to the databse will not be saved

---

## Establishing a connection
`conn = sqlite3.connect('customer.db')` <br><br>
:warning: If a database wasn't previously created, it will now be created as soon as we excute the script

---

## Creating a cursor to perform SQL commands
`c = conn.cursor()`

---

## Creating a table
```python
c.execute(""" CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")
```

:warning: Be sure to use multi-line docstrings `(""" This is a multi-line docstring """)`

---

## Datatypes
* Null
* Integer
* Real
* Text
* Blob

---

## Commiting changes 
`conn.commit()`

---

## Closing the connection
`conn.close()`


---

## Inserting one record at a time
```python
c.execute("INSERT INTO customers VALUES ('John', 'Doe', 'john@email.com')")
```

---

## Inserting multiple rows
```python
customers = [
	('Jason', 'Bourne', 'jason@email.com'), 
	('James', 'Bond', 'james@email'), 
	('Red', 'Sparrow', 'red@email'), 
	('Nathan', 'Muir', 'nathan@email.com')
]

c.executemany("INSERT INTO customers VALUES (?,?,?)", customers)
```

---

## Querying
```python
c.execute("SELECT * FROM customers")

print(c.fetchall())
```

---

## Looping through a query
```python
c.execute("SELECT * FROM customers")

items = c.fetchall()

for item in items:
	print(item)
```

---





