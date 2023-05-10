### A Simple Dictionary
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

------------------------
green
5
```

## Working with Dictionaries
A dictionary in Python is a collection of key-value pairs ( {'color': 'green', 'points': 5} ), it's named pairs because the variable is. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary. <mark style="background: #FFF3A3A6;">The string 'color' is a key in this dictionary, and its associated value is 'green'. </mark>

```py
alien_0 = {'color': 'green', 'points': 5}
```

You can store as many key-value pairs as you want in a dictionary.

### Accessing Values in a Dictionary
```py
alien_0 = {'color': 'green'}
print(alien_0['color'])

---------------------
green
```

### Adding New Key-Value Pairs
The difference between list and dictionaries, is that list are usually in sorted order and dictionaries in arbitrary.
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

----------------------
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
```

### Starting with an Empty Dictionary
It is also possible to work with a empty dictionary. Just like in lists start "list = [ ]", but in this case use braces { }.
```py
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

---------------------
{'color': 'green', 'points': 5}
```

### Modifying Values in a Dictionary
```py
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

-----------------------
The alien is green.
The alien is now yellow.
```
This change is going to make the last value to be forgotten, and can't get back. 

```py
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
	if alien_0['speed'] == 'slow':
		x_increment = 1
	elif alien_0['speed'] == 'medium':
		x_increment = 2
	else:
	# This must be a fast alien.
		x_increment = 3
	# The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

----------------------
Original x-position: 0
New x-position: 2
```
This is a example a something forward in a game.

### Removing Key-Value Pairs
To remove we can use the function "del" too, all del needs is the name of the dictionary and the key that you want to remove.
```py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
u del alien_0['points']
print(alien_0)

------------------------
{'color': 'green', 'points': 5}
{'color': 'green'}
```

### A Dictionary of Similar Objects
You can also use a dictionary to store one kind of information about many objects. 
```py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

----------------------
Sarah's favorite language is C.
```

**Note:** is case you don't have the key it will cause a "KeyError". And if the key doesn't have a value the code won't work causing a "SyntaxError: invalid syntax", and if is empty will show nothing.
**Note - Finding a key:** in case you don't know if you have a key or don't now the value.



## Looping Through a Dictionary