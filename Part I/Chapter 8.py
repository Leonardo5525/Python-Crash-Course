#Defining function
def greet(name):
    print(f'Hello, {name}')

greet('leo')


#Try it yoursel 8-1
def display_message(subject):
    print(f'\nI am learning, {subject}')
display_message('definition')


#Try it yoursel 8-2
def favorite_book(name):
    print(f'\nOne of my favorite books is {name}')
favorite_book('Alice in Boderland')


#Positional arguments and Keyword arguments
def describe_pet(animal_type, pet_name='Pingo'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster')


#Try youself - 1
def make_shirt(size_shirt, message_shirt):
    print(f'\nChoose your shirt size = {size_shirt}')
    print(f'Choose a massage for the shirt = {message_shirt}')

make_shirt('LARGE', 'HELLO')
make_shirt(size_shirt='large', message_shirt='hello')


#Try youself - 2
def make_shirt(size_shirt= 'Large', message_shirt = 'I love Python'):
    print(f'\nChoose your shirt size = {size_shirt}')
    print(f'Choose a massage for the shirt = {message_shirt}')


make_shirt()
make_shirt('medium')
make_shirt('small', 'hello')


#Try youself - 3
def describe_city(name_city, name_country = 'Brazil'):
    print(f'\n{name_city} is in {name_country}')

describe_city('Marilia')
describe_city('Presidente prudente')
describe_city('Osaka', 'Japan')


#Return simple value
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#Making an argument OPTIONAL
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

