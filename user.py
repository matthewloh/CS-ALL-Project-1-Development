import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute("""CREATE TABLE users(
            id integer,
            account_id integer,
            first_name text,
            last_name text,
            email text,
            password text,
            is_registered integer,
            remember_login integer)""")