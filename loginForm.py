import sqlite3

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# c.execute("""CREATE TABLE employees(
#          first_name TEXT,
#          last_name TEXT,
#          pay INTEGER
#          )""")


c.execute('INSERT INTO employees VALUES ("Corey","Schafer", 50000)')

conn.commit()

conn.close()
