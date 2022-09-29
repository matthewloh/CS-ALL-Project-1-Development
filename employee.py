class Employee:
    """A sample Employee class"""

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self) -> str:
        return f"Employee(\'{self.first_name}\', \'{self.last_name}\', {self.pay})" 