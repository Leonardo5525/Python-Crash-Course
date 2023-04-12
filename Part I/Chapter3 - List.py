#Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

#Returning last value on the list or -2 (before the last) -3 (befora -2) and continue
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

#Try ir Yourself - 3-1. Names: 
names = ['leo', 'vitoria', 'joao', 'lucas']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#Try it Yourself - 3-2. Greetings:
names = ['leo naka', 'vitoria', 'joao', 'lucas']
message = (names[0].capitalize())
print(message)

#Try it Yourself - 3-3. Your Own List: 
transportation = ['car', 'motocycle', 'bike', 'airplane']
message = (f'I would like to own a Honda {transportation[0]}')
print(message)

#Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#Appending (last)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

#Appending from a empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting elements into a list (any)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)

#Removing an item using the DEL statement (need to know index)
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

#Removing an Item Using the pop() Method (last, in this case)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Removing Using pop() Method (ANY, in this case)
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing a item by value (any)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)

#Try it Yourself 3-4. Guest List: 
name = ['goro', 'sato', 'miyuki']
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[1]}')
print(f'Please come to my dinner {name[2]}')

#Try it Yourself 3-5. Changing Guest List: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')

#Try it Yourself 3-6. More Guests: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}'
      )
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')

#Try it Yourself 3-7. Shrinking Guest List:
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(f"I understand you can´t make it {cancel_name}")
print('I am sorry my table will not be ready on time')
one_name = name.pop(-4)
two_name = name.pop(-3)
three_name = name.pop(-2)
four_name = name.pop(-1)
print(f'I am sorry that i can note invite you to dinner {one_name}')
print(f'I am sorry that i can note invite you to dinner {two_name}')
print(f'I am sorry that i can note invite you to dinner {three_name}')
print(f'I am sorry that i can note invite you to dinner {four_name}')
print(f'My table still have your seat reserved {name[0]}')
print(f'My table still have your seat reserved {name[1]}')
del name[1]
del name[0]
print(name)

#Try it Yourself 3-7. Shrinking Guest List: NEW WAYS TO DO THE SAME
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(f"I understand you can´t make it {cancel_name}")
print('I am sorry my table will not be ready on time')
one_name = name.pop(-1)
two_name = name.pop(-1)
three_name = name.pop(-1)
four_name = name.pop(-1)
print(f'I am sorry that i can note invite you to dinner {one_name}')
print(f'I am sorry that i can note invite you to dinner {two_name}')
print(f'I am sorry that i can note invite you to dinner {three_name}')
print(f'I am sorry that i can note invite you to dinner {four_name}')
print(f'My table still have your seat reserved {name[0]}')
print(f'My table still have your seat reserved {name[1]}')
del name[0]
del name[0]
print(name)

# Organizing a list using SORT()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse= True)
print(cars)

# Organizing a list using SORTED()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Organizing a list reverse chronological order REVERSE()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Fiding the lenght of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))



#Try it Yourself - 3-8. Seeing the World: 
locals = ['Japan', 'USA', 'Koreia', 'Canada', 'Australia']
print(locals)
print(sorted(locals))
#print(sorted(locals, reverse=True))
print(locals)
locals.reverse()
print(locals)
locals.reverse()
print(locals)
locals.sort()
print(cars)
locals.sort(reverse= True)
print(locals)

# Try it Yourself - 3-9. Dinner Guests: 
name = ['goro', 'sato', 'miyuki']
cancel_name ='goro'
name.remove(cancel_name)
name.append('shimizu')
print(f'Please come to my dinner {name[0]}'
      )
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-1]}')
print(f'I found a bigger table so i am gonna invete some more people')
name.insert(-2, 'mayumura')
name.insert(-2, 'gibson')
name.append('gibson jr')
print(f'Please come to my dinner {name[0]}')
print(f'Please come to my dinner {name[2]}')
print(f"I understand you can´t make it {cancel_name}")
print(f'Please come to my dinner {name[-2]}')
print(f'Please come to my dinner {name[-3]}')
print(f'Please come to my dinner {name[-4]}')
print(f'Please come to my dinner {name[-1]}')
print(len(name))

# Try it Yourself - 3-10. Every Function: 
'''Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.'''

#Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
      print(f'\n{magician}')

#Doing More Work Within a for Loop
magicians = ['alice', 'david', 'carolina']
magicians.sort()
for magician in magicians:
      print(magician.title() + ", that was a great trick!")
      print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#Try it Yourself - 4-1. Pizzas:
pizzas = ['pepperoni', 'cheese', 'margarita']
for pizza in pizzas:
      print(pizza)
      print(f'I love pizza so much {pizza}\n')
print('I love pizza in way that is immeasurable')

#Try it Yourself - 4-2. Animals: 
'''Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.'''
animals = ['dog', 'cat', 'monkey']
for animal in animals:
      print(f'A {animal} is such good pet.\n')
print('All this animals are mammals')

#Using the range() Function
for value in range(1,5):
      print(value)

#Using range() to Make a List of Numbers2
squares = []
for value in range(1,11):
      square = value**2
      squares.append(square)
print(squares)