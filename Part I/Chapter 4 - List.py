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

#Using range() to Make a List of Numbers21
squares = []
for value in range(1,11):
      square = value**2
      squares.append(square)
print(squares)

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (min(digits))
print (max(digits))
print (sum(digits))

#Try it Yourself:
'''4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.'''
for value in range (0,21):
      print(value)

#Try it Yourself:
'''4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)'''
for value in range (1,10):
      print(value)

#Try it Yourself:
'''4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.'''



#Try it Yourself:
'''4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.'''
for valor in range (1,21):
      if valor % 3 == 0:
            print(valor)


#Try it Yourself:
'''4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.'''
for valor in range (0,21,3):
      print(valor)


#Try it Yourself:
'''4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.'''
squares = []
for value in range(1,11):
      square = value**3
      squares.append(square)
print(squares)


#Try it Yourself:
'''4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.'''



# Working with Part of a List
# Slicig a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#Looping Through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)



#Try it Yourself:
'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
  • Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
  • Print the message, Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
  • Print the message, The last three items in the list are:. Use a slice to print the last three items in the list.'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(f'The first 3 items in the list are {players[0:3]}')
print(f'Three items from the middle of the list are {players[1:4]}')
print(f'The last three items in the list are {players[-3:]}')


#Try it Yourself:
'''4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
    •Add a new pizza to the original list.
    •Add a different pizza to the list friend_pizzas.
    •Prove that you have two separate lists. Print the message, My favorite
    pizzas are:, and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list. '''
pizzas = ['pepperoni', 'cheese', 'margarita']
friends_pizzas = pizzas [:]

pizzas.append('muzzarella')
friends_pizzas.append('calabresa')

print("My favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friends_pizzas)


#Try it Yourself:
'''4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.'''



#Turples:
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Looping Through All Values in a Tuple:
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple (in this case you practically create a new turple, losing the values on the first one):
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
