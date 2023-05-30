# Working with Lists
### Looping Through an Entire List

```py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
		print(f'\n{magician}')

----------------------
alice
david
carolina
```


### Doing More Work Within a for Loop

```py
magicians = ['alice', 'david', 'carolina']
magicians.sort()
for magician in magicians:
		print(magician.title() + ", that was a great trick!")
		print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

----------------------
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
David, that was a great trick!
I can't wait to see your next trick, David.
Thank you, everyone. That was a great magic show!
```


### Using the range() Function
Just like in the while loop, in for, when you use range, it's is going to pass for all the numbers stopping just before the last one.
```py
for value in range(1,5):
		print(value)

----------------------
1
2
3
4
```


### Using range() to Make a List of Numbers

```py
squares = []
for value in range(1,11):
		square = value**2
		squares.append(square)
print(squares)

----------------------
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```


### Simple Statistics with a List of Numbers

```py
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (min(digits))
print (max(digits))
print (sum(digits))

----------------------
0
9
45
```

<br>
<br>

## Working with Part of a List

### Slicing a list
When you slice your list you won't lose the list you had at first. Even though it has a particular name indicating it's slicing/ cutting the list, this function will copy and slice where you want it's your choice.
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

----------------------
['charles', 'martina', 'michael']
```

If you omit the first index in a slice, Python automatically starts your slice at the beginning. The same works if you don't add a number to stop.
A negative index returns an element starting a certain distance from the end of a list;
```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:-2])


----------------------
['charles', 'martina', 'michael']
['michael', 'florence', 'eli']
```


### Looping Through a Slice
Specify the index of the first and last elements you want to work with, stopping one item
before the second index you specify.

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
		print(player.title())

----------------------
Here are the first three players on my team:
Charles
Martina
Michael
```


### Copying a List
To copy a list, you can make a slice that includes the entire original list "my_list( [ : ] )" 
```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

----------------------
My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```
When you copy a list, you add her to a variable, which create a new list separate from the first one.


```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
u friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

----------------------
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
```
If you use this example you will add the existing list to a variable, not coping her. This way they will not be separate, so when you add anything to either list, you will add to the another too.

<br>

## Tuples:
This will create a list of items that can't be changed, immutable.
Just like a list except you use parentheses instead of square brackets, and to access using the index is the same too.
When you try to add something will cause a TypeError.
- It's great in cases a line of code tries to change the dimensions of the rectangle, which we don't want.
```py
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

----------------------
200
50
```


### Looping Through All Values in a Tuple:

```
dimensions = (200, 50)
for dimension in dimensions:
		print(dimension)

----------------------
200
50
```
  

### Writing over a Tuples 
Although you can’t modify a tuple, you can assign a new value to a variable
that holds a tuple, redefining the entire tuple:
In this case you practically create a new tuple, but will be losing the values on the first one:

```py
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

----------------------
Original dimensions:
200
50
```

```py
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
		print(dimension)

----------------------
Modified dimensions:
400
100
```

**Note:** When compared with lists, tuples are simple data structures. Set of values that should not be changed through out the life of a program.

## Summary
In this chapter you learned how to work:
- Efficiently with the elements in a list,
- Through a list using a for loop,
- Uses indentation to structure a program, 
- Avoid some common indentation errors, 
- Make simple numerical lists and some operations performing with numerical lists,
- Slice a list to work with a subset of items, 
- Copy lists properly using a slice,
- Tuples, which provide a degree of protection to a set of values that shouldn’t change, and how to style your increasingly complex code to make it easy to read.