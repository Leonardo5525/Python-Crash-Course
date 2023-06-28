class Restaurant:
    '''A simple restaurante class'''

    def __init__(self, restaurant_name, cusine_type):
        self.restaurante_name =  restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Describes a restaurant'''
        print(f'The restaurant is called {self.restaurante_name}')
        print(f'The type is {self.cusine_type}')
    
    def open_restaurant(self):
        '''Describes that restaurantis open'''
        print(f'The restaurant {self.restaurante_name} is open')
    
    def set_restaurant(self, guests):
        '''Describe how nmany people were served'''
        self.number_served = guests
    def set_increment(self, increment):
        self.number_served += increment
    
restaurant = Restaurant(
    input('O nome do restaurante '), 
    input('O tipo de culinária ')
    )
print(f'Number served: {restaurant.number_served}')