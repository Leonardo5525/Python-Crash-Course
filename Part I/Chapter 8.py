'''
Try it yoursel
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
'''
def display_message(subject):
    print(f'\nI am learning, {subject}')
display_message('definition')


'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
'''
def favorite_book(name):
    print(f'\nOne of my favorite books is {name}')
favorite_book('Alice in Boderland')


'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''
def make_shirt(size_shirt, message_shirt):
    print(f'\nChoose your shirt size = {size_shirt}')
    print(f'Choose a massage for the shirt = {message_shirt}')

make_shirt('LARGE', 'HELLO')
make_shirt(size_shirt='large', message_shirt='hello')


'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''
def make_shirt(size_shirt= 'Large', message_shirt = 'I love Python'):
    print(f'\nChoose your shirt size = {size_shirt}')
    print(f'Choose a massage for the shirt = {message_shirt}')


make_shirt()
make_shirt('medium')
make_shirt('small', 'hello')


'''
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
'''
def describe_city(name_city, name_country = 'Brazil'):
    print(f'\n{name_city} is in {name_country}')

describe_city('Marilia')
describe_city('Presidente prudente')
describe_city('Osaka', 'Japan')

'''
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this: "Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that’s returned.
'''
def city_country(name_city, name_country):
    print(f'{name_city} is in {name_country}\n')

city_country('marilia','brazil')
city_country('seattle', 'USA')
city_country('tokyo', 'japan')


'''
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Add an optional parameter to make_album() that allows you to store the number of tracks on an album. If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new function call that includes the number of tracks on an album.
    
'''
def make_Album(artist, song, album=None):
    album = { 'artist': artist, 'album': album, 'song': song}
    return album

print(make_Album('ana castela', 'boiadeira'))
print(make_Album('pearl jam', 'last kiss'))

'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
'''
def make_Album(artist, song, record=None):
    album = { 'artist': artist, 'record': record, 'song': song}
    return album

while True:
    print('Add your favorite artist, song and his album')
    print('If you want to quit the program, press Q')

    artist = input('Artist name: ')
    if artist == 'q':
        break

    record = input('record name: ')
    if artist == 'q':
        break

    song = input('song name: ')
    if artist == 'q':
        break


'''
8-9. Magicians: Make a list of magician’s names. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
'''
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['natsu', 'gray', 'makarov']
show_magicians(magicians)


'''
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9. Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to see that the list has actually been modified.
'''
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def great_magicians(magicians, make_great):
    while magicians:
        name = magicians.pop()
        print(name)
        make_great.append(name)

magicians = ['natsu', 'gray', 'makarov']
make_great = []
great_magicians(magicians, make_great)
print(magicians)
print(make_great)

'''
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the function make_great() with a copy of the list of magicians’ names. Because the original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.
'''
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def great_magicians(magicians, make_great):
    while magicians:
        name = magicians.pop()
        print(name)
        make_great.append(name)

magicians = ['natsu', 'gray', 'makarov']
make_great = []
great_magicians(magicians[:], make_great)
print(magicians)
print(make_great)


'''
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. Call the function three times, using a different number of arguments each time.
'''
def itens_sand(*toppings):
    print ('Your sandwich will have this toppings: ')
    print(f'{toppings} \n')

itens_sand('atum', 'cheese', 'bacon')
itens_sand('tamato', 'lettuce', 'onions')
itens_sand('salmon', 'mayo', 'cream cheese')

'''
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
'''
def build_profile(f_name, last_name, **info):
    profile = {}
    profile['first_name'] = f_name
    profile['last_name'] = last_name
    for key, value in info.items():
        profile[key] = value
    return profile

profile = build_profile('albert', 'einstein', location='princeton' field='physics')
print(profile)


"""
8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary thats returned to make sure all the information was stored correctly.
"""

def build_car(many, model, **info):
    profile = {}
    profile['Manifacture'] = many
    profile['Model'] = model
    for key, value in info.items():
        profile[key] = value
    return profile

car_profile = build_car('fiat', 'GM', location='Marília',color='blue')
print(car_profile)

'''
8-15. Printing Models: Put the functions for the example print_models.py in a separate file called printing_functions.py. Write an import statement at the top of print_models.py, and modify the file to use the imported functions.
'''


'''
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
'''


'''
8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
'''
