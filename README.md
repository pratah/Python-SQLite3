# :arrow_right: Querying data with python :arrow_left:

---

## Establishing a connection in memory
`conn = sqlite3.connect(':memory:')` <br><br>
:warning: Changes made to the databse will not be saved

---

## Establishing a connection
`conn = sqlite3.connect('customer.db')` <br><br>
:warning: If a database wasn't previously created, it will now be created as soon as we excute the script