import sqlite3
from InteractiveSystem import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE employees (
            first_name text,
            last_name text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first_name, :last_name, :pay)", {'first_name': emp.first_name, 'last_name': emp.last_name, 'pay': emp.pay})


def get_emps_by_name(last_namename):
    c.execute("SELECT * FROM employees WHERE last_name=:last_name", {'last_name': last_namename})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first_name = :first_name AND last_name = :last_name""",
                  {'first_name': emp.first_name, 'last_name': emp.last_name, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first_name = :first_name AND last_name = :last_name",
                  {'first_name': emp.first_name, 'last_name': emp.last_name})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close()
