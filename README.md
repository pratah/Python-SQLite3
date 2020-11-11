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


