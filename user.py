class User:
    """A sample User class"""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    

    
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    def __repr__(self) -> str:
        return f"User(\'{self.first_name}\', \'{self.last_name}\', \'{self.email}\', \'{self.password}\')"