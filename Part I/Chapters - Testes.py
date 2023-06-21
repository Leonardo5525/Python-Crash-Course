class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age
        self.city = city
    
    def describe_user (self):
        print(f'The user name is {self.first_name} {self.last_name}')
        print(f'The user is {self.age} years old and lives in {self.city}')
    
    def greet_user(self):
        print(f'Hello {self.first_name}{self.last_name}')
    
user1 = User('leonardo', 'nakamura', 26, 'marilia')
user1.describe_user()
user1.greet_user()


