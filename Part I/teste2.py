class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name =  first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user (self):
        print(f"The user's name is {self.first_name} {self.last_name}")
        print(f'The user is {self.age} years old and lives in {self.city}')
    
    def greet_user(self):
        print (f'Hello {self.first_name}')

class Admin(User):
    def __init__(self, first_name, last_name, age, city, privileges):
        super().__init__(first_name, last_name, age, city)
        self.privileges = privileges
    
    def show_privileges(self):
        print(f'Privileges: ')
        for privilege in self.privileges:
            print(f'- {privilege}')

user =  Admin('leo', 'Admin', 'marilia', 26, ['can add post', 'can delete post', 'can ban user'])
user.describe_user()
user.show_privileges()
    


usuario = User('leo', 'nakamura', 25, 'marilia' )
