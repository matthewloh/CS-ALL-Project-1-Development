import sqlite3

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
conn = sqlite3.connect('registration.db')
class UsersRegistration:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('registration.db')
        self.c = self.conn.cursor()
    #Creating a Table 
    def create_table(self):
        # self.c.execute("""DROP TABLE users""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS users(
                    email TEXT PRIMARY KEY NOT NULL,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    password TEXT NOT NULL
                    )""")
      
    def insert_user(self, item):
        with conn:
            self.c.execute("""INSERT OR IGNORE INTO users VALUES (?,?,?,?)""", item)
            self.conn.commit()

    def get_details(self):
        self.c.execute("SELECT * FROM users")
        return self.c.fetchall()

db = UsersRegistration()
db.create_table()
item = ("email", "first_name", "last_name", "password")
item2 = ("email2", "first_name2", "last_name2", "password2")
db.insert_user(item)
db.insert_user(item2)
