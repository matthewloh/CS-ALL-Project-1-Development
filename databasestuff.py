import sqlite3
from sysconfig import get_scheme_names
from user import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
conn = sqlite3.connect('registration.db')
class User:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('registration.db')
        self.c = self.conn.cursor()
    #Creating a Table 
    def create_table(self):
        # self.c.execute("""DROP TABLE users""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    first_name TEXT,
                    last_name TEXT NOT NULL,
                    password TEXT NOT NULL,
                    PRIMARY KEY(user_id, email)
                    )""")
      
    def insert_user(self, item):
        with conn:
            self.c.execute("""INSERT OR IGNORE INTO users VALUES (?,?,?,?,?,?)""", item)
            self.c.commit()

    def get_user(username):
        c.execute("SELECT * FROM users WHERE username = :username", {'username':username})
        return c.fetchall()

user_1 = User('Matthew', 'Loh', 'matthewloh256@gmail.com', 'password1')
user_ = User(f'{first_name_entry.get()}, {last_name_entry.get()}, {email_entry.get()}{password_entry.get()}')
insert_user(user_1)

conn.close()
