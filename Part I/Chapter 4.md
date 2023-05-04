# Working with Lists
### Looping Through an Entire List

```py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print(f'\n{magician}')
# alice
# david
# carolina
```


### Doing More Work Within a for Loop

```py
magicians = ['alice', 'david', 'carolina']
magicians.sort()
for magician in magicians:
		print(magician.title() + ", that was a great trick!")
		print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#Alice, that was a great trick!
#I can't wait to see your next trick, Alice.
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
# David, that was a great trick!
# I can't wait to see your next trick, David.
# Thank you, everyone. That was a great magic show!
```


### Using the range() Function

```py
for value in range(1,5):
		print(value)
# 1
# 2
# 3
# 4
```


### Using range() to Make a List of Numbers21

```py
squares = []
for value in range(1,11):
		square = value**2
		squares.append(square)
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


### Simple Statistics with a List of Numbers

```py
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (min(digits))
print (max(digits))
print (sum(digits))
# 0
# 9
# 45
```


## Working with Part of a List

### Slicig a list

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# ['charles', 'martina', 'michael']
```


### Looping Through a Slice

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
		print(player.title())
# Here are the first three players on my team:
# Charles
# Martina
# Michael
```


  
### Copying a List

```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake']

#My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake']
```


## Turples:

```py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 200
# 50
```


### Looping Through All Values in a Tuple:

```
dimensions = (200, 50)
for dimension in dimensions:
		print(dimension)
# 200
# 50
```
  

### Writing over a Tuples 
In this case you practically create a new tuples, losing the values on the first one:

```py
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
# Original dimensions:
# 200
# 50
```

```py
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
		print(dimension)
# Modified dimensions:
# 400
# 100
```
